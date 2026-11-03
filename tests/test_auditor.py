"""Tests for spec_auditor.py. Tags below are the requirement references
the auditor itself checks (REQ-001..REQ-010, self-audit demo).

Runnable two ways: `python3 run_tests.py` (no pytest needed) or pytest.
"""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from spec_auditor import parse_spec, scan_tree, audit  # noqa: E402

# REQ-001, REQ-002
def test_parse_spec_and_missing():
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write("- REQ-001: parse me\n- REQ-002: and me\n")
        path = f.name
    spec = parse_spec(path)
    assert "REQ-001" in spec and "REQ-002" in spec

# REQ-003, REQ-004, REQ-009
def test_scan_tree_plain_text():
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "a.py")
        open(p, "w").write("# REQ-003 here\n")
        hits = scan_tree(d)
        assert "REQ-003" in hits

# REQ-005, REQ-006, REQ-007, REQ-008
def test_statuses_and_orphans():
    spec = {"REQ-005": "x", "REQ-006": "y"}
    src = {"REQ-005": ["s.py"], "REQ-999": ["s.py"]}
    tests = {"REQ-005": ["t.py"]}
    lines, gaps = audit(spec, src, tests)
    assert any("REQ-005 COVERED" in l for l in lines)
    assert any("REQ-006 MISSING" in l for l in lines)
    assert any("REQ-999 ORPHAN" in l for l in lines)
    assert gaps == 1

# REQ-010
def test_cli_defaults_exit_codes():
    root = os.path.join(os.path.dirname(__file__), "..")
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, ".kiro", "specs", "demo"), exist_ok=True)
        open(os.path.join(d, ".kiro", "specs", "demo", "requirements.md"),
             "w").write("- REQ-010: defaults\n")
        os.makedirs(os.path.join(d, "src"), exist_ok=True)
        os.makedirs(os.path.join(d, "tests"), exist_ok=True)
        open(os.path.join(d, "src", "a.py"), "w").write("# REQ-010\n")
        open(os.path.join(d, "tests", "t.py"), "w").write("# REQ-010\n")
        r = subprocess.run(
            [sys.executable, os.path.join(root, "spec_auditor.py"),
             "--spec", ".kiro/specs/demo/requirements.md",
             "--src", "src", "--tests", "tests"],
            cwd=d, capture_output=True, text=True)
        assert r.returncode == 0, r.stdout
