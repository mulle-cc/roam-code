"""Objective-C symbol and reference extractor (Tier 1).

Extends CExtractor since the tree-sitter-objc grammar is a superset of C.
Handles @interface, @implementation, @protocol, method declarations/definitions,
@property, message expressions, and @import.
"""

from __future__ import annotations

from .c_lang import CExtractor


class ObjCExtractor(CExtractor):
    """Objective-C extractor extending C with ObjC-specific constructs."""

    @property
    def language_name(self) -> str:
        return "objc"

    @property
    def file_extensions(self) -> list[str]:
        return [".m", ".mm"]

    # ---- Symbol extraction ----

    def _walk_symbols(self, node, source, symbols, parent_name, is_header):
        for child in node.children:
            t = child.type
            if t == "class_interface":
                self._extract_class_interface(child, source, symbols)
            elif t == "class_implementation":
                self._extract_class_implementation(child, source, symbols)
            elif t == "protocol_declaration":
                self._extract_protocol(child, source, symbols)
            else:
                # Delegate C constructs (functions, structs, enums, typedefs) to CExtractor
                # We call the parent's per-node handlers directly rather than recursing
                # through _walk_symbols to avoid double-visiting.
                from roam.languages.c_lang import CExtractor as _C
                if t == "function_definition":
                    _C._extract_function(self, child, source, symbols, parent_name, is_header)
                elif t == "declaration":
                    _C._extract_declaration(self, child, source, symbols, parent_name, is_header)
                elif t == "struct_specifier":
                    _C._extract_struct(self, child, source, symbols, parent_name, is_header, kind="struct")
                elif t == "union_specifier":
                    _C._extract_struct(self, child, source, symbols, parent_name, is_header, kind="struct")
                elif t == "enum_specifier":
                    _C._extract_enum(self, child, source, symbols, parent_name, is_header)
                elif t == "type_definition":
                    _C._extract_typedef(self, child, source, symbols, parent_name, is_header)

    def _class_name(self, node, source) -> str:
        """First identifier child = class name."""
        for child in node.children:
            if child.type == "identifier":
                return self.node_text(child, source)
        return ""

    def _superclass_name(self, node, source) -> str | None:
        """Identifier after ':' in class_interface / class_implementation."""
        found_colon = False
        for child in node.children:
            if child.type == ":" :
                found_colon = True
            elif found_colon and child.type == "identifier":
                return self.node_text(child, source)
        return None

    def _category_name(self, node, source) -> str | None:
        """Identifier inside '(' ')' for categories."""
        in_paren = False
        for child in node.children:
            if child.type == "(":
                in_paren = True
            elif in_paren and child.type == "identifier":
                return self.node_text(child, source)
            elif child.type == ")":
                break
        return None

    def _is_category(self, node, source) -> bool:
        for child in node.children:
            if child.type == "(":
                return True
        return False

    def _protocol_names(self, node, source) -> list[str]:
        """Protocol names from parameterized_arguments <P1, P2>."""
        for child in node.children:
            if child.type == "parameterized_arguments":
                return [
                    self.node_text(c, source)
                    for c in child.children
                    if c.type in ("type_name", "type_identifier", "identifier")
                    and self.node_text(c, source) not in ("<", ">", ",")
                ]
        return []

    def _extract_class_interface(self, node, source, symbols):
        name = self._class_name(node, source)
        if not name:
            return

        is_category = self._is_category(node, source)
        cat = self._category_name(node, source) if is_category else None
        qualified = f"{name}({cat})" if cat else name
        superclass = None if is_category else self._superclass_name(node, source)
        protocols = self._protocol_names(node, source)

        sig = f"@interface {qualified}"
        if superclass:
            sig += f" : {superclass}"
        if protocols:
            sig += f" <{', '.join(protocols)}>"

        symbols.append(self._make_symbol(
            name=qualified,
            kind="class",
            line_start=node.start_point[0] + 1,
            line_end=node.end_point[0] + 1,
            signature=sig,
            docstring=self.get_docstring(node, source),
            is_exported=True,
        ))

        # Methods and properties declared in the interface
        for child in node.children:
            if child.type == "method_declaration":
                self._extract_method_decl(child, source, symbols, qualified)
            elif child.type == "property_declaration":
                self._extract_property(child, source, symbols, qualified)
            elif child.type == "instance_variables":
                self._extract_ivars(child, source, symbols, qualified)

    def _extract_class_implementation(self, node, source, symbols):
        name = self._class_name(node, source)
        if not name:
            return

        is_category = self._is_category(node, source)
        cat = self._category_name(node, source) if is_category else None
        qualified = f"{name}({cat})" if cat else name

        # Only emit a class symbol if there's no matching @interface
        # (implementations without a separate header are self-contained)
        symbols.append(self._make_symbol(
            name=qualified,
            kind="class",
            line_start=node.start_point[0] + 1,
            line_end=node.end_point[0] + 1,
            signature=f"@implementation {qualified}",
            is_exported=False,
        ))

        for child in node.children:
            if child.type == "implementation_definition":
                for impl_child in child.children:
                    if impl_child.type == "method_definition":
                        self._extract_method_def(impl_child, source, symbols, qualified)
            elif child.type == "method_definition":
                self._extract_method_def(child, source, symbols, qualified)

    def _extract_protocol(self, node, source, symbols):
        name = ""
        for child in node.children:
            if child.type == "identifier":
                name = self.node_text(child, source)
                break
        if not name:
            return

        symbols.append(self._make_symbol(
            name=name,
            kind="interface",
            line_start=node.start_point[0] + 1,
            line_end=node.end_point[0] + 1,
            signature=f"@protocol {name}",
            docstring=self.get_docstring(node, source),
            is_exported=True,
        ))

        for child in node.children:
            if child.type == "method_declaration":
                self._extract_method_decl(child, source, symbols, name)

    def _build_selector(self, node, source) -> str:
        """Build ObjC selector string from a method_declaration or method_definition node.

        Simple selector:  - (void)doSomething  → "doSomething"
        Keyword selector: - (void)foo:(int)x bar:(int)y → "foo:bar:"
        """
        parts = []
        i = 0
        children = node.children
        while i < len(children):
            child = children[i]
            if child.type == "identifier" and not parts:
                # First identifier = selector start (before any method_parameter)
                # Check if next sibling is a method_parameter (keyword selector)
                next_sibling = children[i + 1] if i + 1 < len(children) else None
                if next_sibling and next_sibling.type == "method_parameter":
                    parts.append(self.node_text(child, source))
                else:
                    # Simple selector — no colon
                    return self.node_text(child, source)
            elif child.type == "method_parameter":
                # Each method_parameter contributes a ':'
                # Look for a preceding keyword identifier
                if i > 0 and children[i - 1].type == "identifier" and parts:
                    parts[-1] += ":"
                elif parts:
                    parts[-1] += ":"
                else:
                    parts.append(":")
                # Check for next keyword part (identifier before next method_parameter)
                if i + 1 < len(children) and children[i + 1].type == "identifier":
                    parts.append(self.node_text(children[i + 1], source))
                    i += 1  # skip that identifier on next iteration
            i += 1
        return "".join(parts) if parts else ""

    def _method_return_type(self, node, source) -> str:
        for child in node.children:
            if child.type == "method_type":
                for tc in child.children:
                    if tc.type == "type_name":
                        return self.node_text(tc, source)
        return "void"

    def _method_is_class(self, node, source) -> bool:
        for child in node.children:
            if self.node_text(child, source) == "+":
                return True
        return False

    def _extract_method_decl(self, node, source, symbols, parent_name):
        selector = self._build_selector(node, source)
        if not selector:
            return
        prefix = "+" if self._method_is_class(node, source) else "-"
        ret = self._method_return_type(node, source)
        sig = f"{prefix} ({ret}){selector}"

        symbols.append(self._make_symbol(
            name=selector,
            kind="method",
            line_start=node.start_point[0] + 1,
            line_end=node.end_point[0] + 1,
            qualified_name=f"{parent_name}.{selector}",
            signature=sig,
            is_exported=True,
            parent_name=parent_name,
        ))

    def _extract_method_def(self, node, source, symbols, parent_name):
        selector = self._build_selector(node, source)
        if not selector:
            return
        prefix = "+" if self._method_is_class(node, source) else "-"
        ret = self._method_return_type(node, source)
        sig = f"{prefix} ({ret}){selector}"

        symbols.append(self._make_symbol(
            name=selector,
            kind="method",
            line_start=node.start_point[0] + 1,
            line_end=node.end_point[0] + 1,
            qualified_name=f"{parent_name}.{selector}",
            signature=sig,
            is_exported=False,
            parent_name=parent_name,
        ))

    def _extract_property(self, node, source, symbols, parent_name):
        """Extract @property name from struct_declaration inside property_declaration."""
        for child in node.children:
            if child.type == "struct_declaration":
                for sc in child.children:
                    if sc.type == "struct_declarator":
                        # Name is inside pointer_declarator or field_identifier
                        name = self._declarator_name(sc, source)
                        if name:
                            sig = f"@property {self.node_text(node, source).split(';')[0].strip()}"
                            symbols.append(self._make_symbol(
                                name=name,
                                kind="property",
                                line_start=node.start_point[0] + 1,
                                line_end=node.end_point[0] + 1,
                                qualified_name=f"{parent_name}.{name}",
                                signature=sig,
                                is_exported=True,
                                parent_name=parent_name,
                            ))

    def _declarator_name(self, node, source) -> str | None:
        """Recursively find the identifier name inside a declarator."""
        if node.type in ("field_identifier", "identifier"):
            return self.node_text(node, source)
        for child in node.children:
            name = self._declarator_name(child, source)
            if name:
                return name
        return None

    def _extract_ivars(self, node, source, symbols, parent_name):
        """Extract instance variables from { ... } block."""
        for child in node.children:
            if child.type == "instance_variable":
                for iv_child in child.children:
                    if iv_child.type == "struct_declaration":
                        for sc in iv_child.children:
                            if sc.type == "struct_declarator":
                                name = self._declarator_name(sc, source)
                                if name:
                                    symbols.append(self._make_symbol(
                                        name=name,
                                        kind="field",
                                        line_start=iv_child.start_point[0] + 1,
                                        line_end=iv_child.end_point[0] + 1,
                                        qualified_name=f"{parent_name}.{name}",
                                        parent_name=parent_name,
                                    ))

    # ---- Reference extraction ----

    def _walk_refs(self, node, source, refs, scope_name):
        for child in node.children:
            t = child.type
            if t == "message_expression":
                self._extract_message(child, source, refs, scope_name)
                self._walk_refs(child, source, refs, scope_name)
            elif t == "module_import":
                self._extract_module_import(child, source, refs, scope_name)
            elif t == "class_interface":
                self._extract_interface_refs(child, source, refs)
            elif t == "preproc_include":
                self._extract_include(child, source, refs, scope_name)
            elif t == "call_expression":
                self._extract_call(child, source, refs, scope_name)
            else:
                new_scope = scope_name
                if t == "method_definition":
                    sel = self._build_selector(child, source)
                    if sel:
                        new_scope = sel
                self._walk_refs(child, source, refs, new_scope)

    def _extract_message(self, node, source, refs, scope_name):
        """[receiver method] or [receiver keyword:arg ...]"""
        children = [c for c in node.children if c.type not in ("[", "]")]
        if not children:
            return
        # All identifier children after the receiver are method name parts
        # receiver is first child; method identifiers follow
        for i, child in enumerate(children):
            if i == 0:
                continue  # skip receiver
            if child.type == "identifier":
                refs.append(self._make_reference(
                    target_name=self.node_text(child, source),
                    kind="call",
                    line=child.start_point[0] + 1,
                    source_name=scope_name,
                ))
                break  # first method identifier is enough

    def _extract_module_import(self, node, source, refs, scope_name):
        """@import Module.SubModule"""
        parts = [self.node_text(c, source) for c in node.children
                 if c.type == "identifier"]
        if parts:
            path = ".".join(parts)
            refs.append(self._make_reference(
                target_name=parts[0],
                kind="import",
                line=node.start_point[0] + 1,
                source_name=scope_name,
                import_path=path,
            ))

    def _extract_interface_refs(self, node, source, refs):
        """Emit inherits refs for superclass and protocol conformances."""
        name = self._class_name(node, source)
        if not name:
            return
        superclass = self._superclass_name(node, source)
        if superclass:
            refs.append(self._make_reference(
                target_name=superclass,
                kind="inherits",
                line=node.start_point[0] + 1,
                source_name=name,
            ))
        for proto in self._protocol_names(node, source):
            refs.append(self._make_reference(
                target_name=proto,
                kind="inherits",
                line=node.start_point[0] + 1,
                source_name=name,
            ))
