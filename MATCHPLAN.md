# MATCHPLAN: Objective-C Language Support (Tier 1)

## Goal

Add Objective-C as a Tier 1 language to roam-code with full symbol extraction, reference tracking, and inheritance support.

## Grammar Source

**tree-sitter-objc** via `tree-sitter-language-pack` (already available as `"objc"`). No additional dependency needed.

The grammar extends tree-sitter-c, so ObjC AST nodes are a superset of C nodes. A local ANTLR grammar exists at `/home/src/srcO/mulle-cc/mulle-ts/src/ObjC.g4` — used as a reference for Objective-C language constructs, not as a parser.

## AST Node Mapping

Verified by parsing sample ObjC code through `tree-sitter-language-pack get_parser('objc')`:

### Symbols to Extract

| ObjC Construct | tree-sitter node type | roam kind | Notes |
|---|---|---|---|
| `@interface Foo : Bar` | `class_interface` → child `identifier` | `class` | Superclass via `:` + `identifier`. Protocols via `parameterized_arguments` (`<Proto>`) |
| `@interface Foo (Cat)` | `class_interface` with `(` category `)` | `class` | Category — qualified as `Foo(Cat)` |
| `@implementation Foo` | `class_implementation` → child `identifier` | `class` | Only emit if no matching `@interface` seen |
| `@protocol Foo` | `protocol_declaration` → child `identifier` | `interface` | Protocol ≈ interface |
| `+ (type)name` (decl) | `method_declaration` with `+` | `method` | Class method. Build selector from `identifier` + `method_parameter` colons |
| `- (type)name` (decl) | `method_declaration` with `-` | `method` | Instance method |
| `+ (type)name { ... }` | `method_definition` with `+` | `method` | Class method definition (inside `@implementation`) |
| `- (type)name { ... }` | `method_definition` with `-` | `method` | Instance method definition |
| `@property (...) T *name` | `property_declaration` → `struct_declaration` | `property` | Extract name from `struct_declarator` |
| `void func(int x) { }` | `function_definition` | `function` | C functions — reuse CExtractor logic |
| `typedef ...` | `type_definition` | `type_alias` | Reuse CExtractor logic |
| `struct Foo { }` | `struct_specifier` | `struct` | Reuse CExtractor logic |
| `enum Foo { }` | `enum_specifier` | `enum` | Reuse CExtractor logic |
| Instance variables | `instance_variables` → `struct_declaration` | `field` | `{ int _count; }` block |

### References to Extract

| ObjC Construct | tree-sitter node type | roam ref kind | Notes |
|---|---|---|---|
| `#import <F/F.h>` | `preproc_include` with `#import` | `import` | Same as C `#include` |
| `#import "foo.h"` | `preproc_include` with `#import` | `import` | Local import |
| `@import Module` | `module_import` | `import` | Module import (modern ObjC) |
| `[obj method]` | `message_expression` → `identifier` (receiver) + `identifier` (method) | `call` | Message send |
| `[self method]` | `message_expression` with `self` receiver | `call` | Self-call |
| `[ClassName method]` | `message_expression` with class receiver | `call` | Class method call |
| `func(args)` | `call_expression` | `call` | C function call — reuse CExtractor |
| `: SuperClass` | superclass `identifier` in `class_interface` | `inherits` | Inheritance |
| `<Protocol>` | `parameterized_arguments` identifiers | `inherits` | Protocol conformance |

### Selector Name Construction

ObjC methods have multi-part selectors: `- (void)insertObject:(id)obj atIndex:(NSUInteger)idx` → selector = `insertObject:atIndex:`.

From the AST, the selector is built by concatenating:
- The first `identifier` child (before any `method_parameter`)
- A `:` for each `method_parameter` node
- Any `identifier` children of subsequent `method_parameter` keyword parts

## Implementation Plan

### 1. Create `src/roam/languages/objc_lang.py`

New `ObjCExtractor(CExtractor)` class extending the C extractor (like `CppExtractor` does), adding:

- `language_name` → `"objc"`
- `file_extensions` → `[".m", ".mm", ".h"]` (`.h` shared with C — see conflict resolution below)
- Override `_walk_symbols()` to handle ObjC-specific nodes (`class_interface`, `class_implementation`, `protocol_declaration`, `method_declaration`, `method_definition`, `property_declaration`) while delegating C nodes to `super()`
- Override `_walk_refs()` to handle `message_expression`, `module_import`, while delegating C refs to `super()`
- Helper `_build_selector()` to construct ObjC selector strings from AST nodes
- Helper `_extract_method_signature()` to build `- (ReturnType)selector:(ParamType)param` strings

### 2. Register in `src/roam/languages/registry.py`

- Add to `_EXTENSION_MAP`: `".m": "objc"`, `".mm": "objc"`
- Add `"objc"` to `_DEDICATED_EXTRACTORS`
- Add `"objc"` to `_SUPPORTED_LANGUAGES`
- Add `elif language == "objc":` branch in `_create_extractor()`
- **`.h` handling**: `get_language_for_file()` checks `roam config h-language` for `.h` files. Defaults to `"c"` if unset. After `roam config h-language objc`, `.h` → `"objc"` and a `roam index --force` picks it up.

### 3. Register grammar in `src/roam/index/parser.py`

No alias needed — `"objc"` is a native grammar in `tree-sitter-language-pack`. Just ensure `"objc"` is not in `REGEX_ONLY_LANGUAGES` (it won't be).

### 4. Create `tests/test_objc.py`

Test cases:
- Class interface with superclass and protocol conformance
- Category interface
- Class/instance method declarations and definitions (including multi-part selectors)
- Properties
- `#import` and `@import` references
- Message expression references (`[obj method]`, `[self method]`, `[ClassName method]`)
- Inheritance edges (superclass + protocol)
- C functions and structs inside `.m` files (inherited from CExtractor)
- Integration test: index a small ObjC project, verify `roam file`, `roam symbol`, `roam deps`

### 5. Update documentation

- Add Objective-C row to Tier 1 table in `README.md`
- Update `AGENTS.md` language list

## `.h` Header Language Config

Since ObjC (and C++) are strict supersets of C, parsing `.h` files with the ObjC or C++ grammar is harmless. A persistent config option controls the mapping:

```bash
roam config h-language objc   # .h files parsed as Objective-C
roam config h-language cpp    # .h files parsed as C++
roam config h-language c      # default
```

Implementation: `get_language_for_file()` in `registry.py` checks the config value for `.h` files instead of hardcoding `"c"`. The config is read from `.roam/config.json` (already used by `roam config`).

## ANTLR Grammar Reference

The local `/home/src/srcO/mulle-cc/mulle-ts/src/ObjC.g4` confirms the following ObjC constructs that the tree-sitter grammar also covers:
- `class_interface`, `class_implementation`, `category_interface`, `category_implementation`
- `protocol_declaration`, `protocol_declaration_list`, `class_declaration_list`
- `method_declaration` (class `+` / instance `-`), `method_definition`
- `property_declaration` with `property_attributes_declaration`
- `message_expression` with `receiver` + `message_selector`
- `selector_expression` (`@selector(...)`)
- `protocol_reference_list` (`<Proto1, Proto2>`)
- `instance_variables` with `visibility_specification`

The ANTLR grammar uses different rule names but maps 1:1 to the tree-sitter node types verified above.

## Estimated Effort

- `objc_lang.py`: ~250 lines (leveraging CExtractor inheritance)
- `registry.py` changes: ~10 lines
- `test_objc.py`: ~200 lines
- `README.md` / `AGENTS.md`: ~5 lines each
