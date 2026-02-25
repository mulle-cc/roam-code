"""Tests for Objective-C language extractor."""

from __future__ import annotations

import pytest
from click.testing import CliRunner

from roam.languages.objc_lang import ObjCExtractor
from roam.languages.registry import get_language_for_file


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_objc(source: str):
    from tree_sitter_language_pack import get_parser
    parser = get_parser("objc")
    return parser.parse(source.encode())


def symbols(source: str) -> list[dict]:
    extractor = ObjCExtractor()
    tree = parse_objc(source)
    return extractor.extract_symbols(tree, source.encode(), "test.m")


def refs(source: str) -> list[dict]:
    extractor = ObjCExtractor()
    tree = parse_objc(source)
    return extractor.extract_references(tree, source.encode(), "test.m")


def sym_names(source: str) -> list[str]:
    return [s["name"] for s in symbols(source)]


def ref_targets(source: str, kind: str | None = None) -> list[str]:
    return [r["target_name"] for r in refs(source) if kind is None or r["kind"] == kind]


# ---------------------------------------------------------------------------
# Extension mapping
# ---------------------------------------------------------------------------

class TestExtensionMapping:
    def test_m_maps_to_objc(self):
        assert get_language_for_file("foo.m") == "objc"

    def test_mm_maps_to_objc(self):
        assert get_language_for_file("foo.mm") == "objc"

    def test_aam_maps_to_objc(self):
        assert get_language_for_file("foo.aam") == "objc"

    def test_h_defaults_to_c(self):
        assert get_language_for_file("foo.h") == "c"


# ---------------------------------------------------------------------------
# Class interface
# ---------------------------------------------------------------------------

class TestClassInterface:
    def test_simple_class(self):
        src = """
@interface MyClass : NSObject
@end
"""
        assert "MyClass" in sym_names(src)

    def test_class_kind(self):
        src = "@interface MyClass : NSObject\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "MyClass")
        assert s["kind"] == "class"
        assert s["is_exported"] is True

    def test_class_signature(self):
        src = "@interface MyClass : NSObject\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "MyClass")
        assert "@interface MyClass" in s["signature"]
        assert "NSObject" in s["signature"]

    def test_category(self):
        src = "@interface MyClass (Helpers)\n@end\n"
        assert "MyClass(Helpers)" in sym_names(src)

    def test_protocol_conformance_in_signature(self):
        src = "@interface MyClass : NSObject <MyProtocol>\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "MyClass")
        assert "MyProtocol" in s["signature"]


# ---------------------------------------------------------------------------
# Protocol
# ---------------------------------------------------------------------------

class TestProtocol:
    def test_protocol_extracted(self):
        src = "@protocol MyProtocol\n- (void)doIt;\n@end\n"
        assert "MyProtocol" in sym_names(src)

    def test_protocol_kind(self):
        src = "@protocol MyProtocol\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "MyProtocol")
        assert s["kind"] == "interface"

    def test_protocol_method_extracted(self):
        src = "@protocol MyProtocol\n- (void)doIt;\n+ (id)create;\n@end\n"
        names = sym_names(src)
        assert "doIt" in names
        assert "create" in names

    def test_protocol_method_parent(self):
        src = "@protocol MyProtocol\n- (void)doIt;\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "doIt")
        assert s["parent_name"] == "MyProtocol"


# ---------------------------------------------------------------------------
# Method declarations (in @interface)
# ---------------------------------------------------------------------------

class TestMethodDeclarations:
    def test_instance_method(self):
        src = "@interface Foo : NSObject\n- (void)doSomething;\n@end\n"
        assert "doSomething" in sym_names(src)

    def test_class_method(self):
        src = "@interface Foo : NSObject\n+ (instancetype)sharedInstance;\n@end\n"
        assert "sharedInstance" in sym_names(src)

    def test_method_kind(self):
        src = "@interface Foo : NSObject\n- (void)doSomething;\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "doSomething")
        assert s["kind"] == "method"
        assert s["parent_name"] == "Foo"

    def test_method_signature_instance(self):
        src = "@interface Foo : NSObject\n- (void)doSomething;\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "doSomething")
        assert s["signature"].startswith("- (void)doSomething")

    def test_method_signature_class(self):
        src = "@interface Foo : NSObject\n+ (instancetype)sharedInstance;\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "sharedInstance")
        assert s["signature"].startswith("+ (instancetype)sharedInstance")

    def test_keyword_selector(self):
        src = "@interface Foo : NSObject\n- (void)insertObject:(id)obj atIndex:(NSUInteger)idx;\n@end\n"
        names = sym_names(src)
        assert any("insertObject:" in n for n in names)

    def test_keyword_selector_full(self):
        src = "@interface Foo : NSObject\n- (void)insertObject:(id)obj atIndex:(NSUInteger)idx;\n@end\n"
        s = next(s for s in symbols(src) if "insertObject:" in s["name"])
        assert s["name"] == "insertObject:atIndex:"


# ---------------------------------------------------------------------------
# Method definitions (in @implementation)
# ---------------------------------------------------------------------------

class TestMethodDefinitions:
    def test_method_def_extracted(self):
        src = """
@implementation MyClass
- (void)doSomething {
}
@end
"""
        assert "doSomething" in sym_names(src)

    def test_class_method_def(self):
        src = """
@implementation MyClass
+ (instancetype)sharedInstance {
    return nil;
}
@end
"""
        assert "sharedInstance" in sym_names(src)

    def test_method_def_parent(self):
        src = """
@implementation MyClass
- (void)doSomething {
}
@end
"""
        s = next(s for s in symbols(src) if s["name"] == "doSomething")
        assert s["parent_name"] == "MyClass"

    def test_category_method_def(self):
        src = """
@implementation MyClass (Helpers)
- (void)helperMethod {
}
@end
"""
        names = sym_names(src)
        assert "helperMethod" in names
        s = next(s for s in symbols(src) if s["name"] == "helperMethod")
        assert s["parent_name"] == "MyClass(Helpers)"


# ---------------------------------------------------------------------------
# Properties
# ---------------------------------------------------------------------------

class TestProperties:
    def test_property_extracted(self):
        src = "@interface Foo : NSObject\n@property (nonatomic, strong) NSString *name;\n@end\n"
        assert "name" in sym_names(src)

    def test_property_kind(self):
        src = "@interface Foo : NSObject\n@property (nonatomic, strong) NSString *name;\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "name")
        assert s["kind"] == "property"
        assert s["parent_name"] == "Foo"

    def test_property_without_attributes(self):
        src = "@interface Foo : NSObject\n@property NSInteger count;\n@end\n"
        assert "count" in sym_names(src)


class TestInstanceVariables:
    def test_ivar_extracted(self):
        src = "@interface Foo : NSObject {\n    int _count;\n}\n@end\n"
        assert "_count" in sym_names(src)

    def test_ivar_kind(self):
        src = "@interface Foo : NSObject {\n    int _count;\n}\n@end\n"
        s = next(s for s in symbols(src) if s["name"] == "_count")
        assert s["kind"] == "field"
        assert s["parent_name"] == "Foo"


# ---------------------------------------------------------------------------
# C constructs still work
# ---------------------------------------------------------------------------

class TestCConstructs:
    def test_c_function(self):
        src = "void freeFunction(int x) { }\n"
        assert "freeFunction" in sym_names(src)

    def test_c_struct(self):
        src = "struct Point { int x; int y; };\n"
        assert "Point" in sym_names(src)


# ---------------------------------------------------------------------------
# References
# ---------------------------------------------------------------------------

class TestReferences:
    def test_import_angle(self):
        src = "#import <Foundation/Foundation.h>\n"
        assert any("Foundation" in t for t in ref_targets(src, "import"))

    def test_module_import(self):
        src = "@import Foundation;\n"
        assert "Foundation" in ref_targets(src, "import")

    def test_message_expression_call(self):
        src = """
@implementation Foo
- (void)bar {
    [self doSomething];
}
@end
"""
        assert "doSomething" in ref_targets(src, "call")

    def test_class_message_call(self):
        src = """
@implementation Foo
- (void)bar {
    [NSObject alloc];
}
@end
"""
        assert "alloc" in ref_targets(src, "call")

    def test_inherits_superclass(self):
        src = "@interface MyClass : NSObject\n@end\n"
        assert "NSObject" in ref_targets(src, "inherits")

    def test_inherits_protocol(self):
        src = "@interface MyClass : NSObject <MyProtocol>\n@end\n"
        assert "MyProtocol" in ref_targets(src, "inherits")


# ---------------------------------------------------------------------------
# Integration: index a small ObjC project
# ---------------------------------------------------------------------------

class TestHLanguageConfig:
    def test_h_language_config(self, tmp_path):
        """roam config --c-dialect objc persists and affects get_language_for_file."""
        import subprocess, sys
        from pathlib import Path
        proj = tmp_path / "proj"
        proj.mkdir()
        subprocess.run(["git", "init"], cwd=proj, capture_output=True)
        roam_bin = str(Path(sys.executable).parent / "roam")
        result = subprocess.run(
            [roam_bin, "config", "--c-dialect", "objc"],
            cwd=proj, capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert "objc" in result.stdout
        import json
        cfg = json.loads((proj / ".roam" / "config.json").read_text())
        assert cfg["c-dialect"] == "objc"

    def test_h_language_invalid(self, tmp_path):
        import subprocess, sys
        from pathlib import Path
        proj = tmp_path / "proj"
        proj.mkdir()
        subprocess.run(["git", "init"], cwd=proj, capture_output=True)
        roam_bin = str(Path(sys.executable).parent / "roam")
        result = subprocess.run(
            [roam_bin, "config", "--c-dialect", "java"],
            cwd=proj, capture_output=True, text=True,
        )
        assert result.returncode != 0


class TestIntegration:
    def test_index_and_query(self, tmp_path):
        import subprocess, sys
        from pathlib import Path
        proj = tmp_path / "myproj"
        proj.mkdir()
        subprocess.run(["git", "init"], cwd=proj, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=proj, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=proj, capture_output=True)
        (proj / "Foo.m").write_text("""
#import <Foundation/Foundation.h>

@interface Foo : NSObject
- (void)hello;
@end

@implementation Foo
- (void)hello {
    NSLog(@"hi");
}
@end
""")
        subprocess.run(["git", "add", "."], cwd=proj, capture_output=True)
        subprocess.run(["git", "commit", "-m", "init"], cwd=proj, capture_output=True)

        venv_python = sys.executable
        roam_bin = str(Path(sys.executable).parent / "roam")

        result = subprocess.run(
            [roam_bin, "index"],
            cwd=proj, capture_output=True, text=True,
        )
        assert result.returncode == 0

        result = subprocess.run(
            [roam_bin, "file", "Foo.m"],
            cwd=proj, capture_output=True, text=True,
        )
        assert "Foo" in result.stdout
        assert "hello" in result.stdout
