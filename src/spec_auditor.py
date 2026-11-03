#!/usr/bin/env python3
"""Kiro Spec Auditor: check that every REQ-XXX in a spec is referenced
by source code and by tests. Stdlib only, no network.

Usage:
    python3 spec_auditor.py [--spec PATH] [--src DIR] [--tests DIR]

Defaults: spec = first requirements.md under .kiro/specs/,
src = src/, tests = tests/. Exit 0 = all covered, 1 = gaps, 2 = usage error.
"""
import argparse
import os
import re
import sys

TAG_RE = re.compile(r"REQ-\d+")
MAX_BYTES = 1_000_000
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv"}


def parse_spec(path):
    """REQ-001, REQ-002: extract tags + statements, or fail loudly."""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"error: cannot read spec file {path}: {e}", file=sys.stderr)
        sys.exit(2)
    spec = {}
    for line in text.splitlines():
        for tag in TAG_RE.findall(line):
            if tag not in spec:
                stmt = line.strip()
                spec[tag] = stmt[:120]
    return spec


def scan_tree(root):
    """REQ-003, REQ-004, REQ-009: plain substring tag search over text files."""
    hits = {}
    if not os.path.isdir(root):
        return hits
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            path = os.path.join(dirpath, name)
            try:
                if os.path.getsize(path) > MAX_BYTES:
                    continue
                with open(path, encoding="utf-8", errors="strict") as f:
                    text = f.read()
            except (OSError, UnicodeDecodeError):
                continue
            for tag in set(TAG_RE.findall(text)):
                hits.setdefault(tag, []).append(os.path.relpath(path))
    return hits


def audit(spec, src_hits, test_hits):
    """REQ-005, REQ-006, REQ-007, REQ-008: statuses + orphans + exit logic."""
    lines = []
    gaps = 0
    for tag in sorted(spec):
        in_src = tag in src_hits
        in_tests = tag in test_hits
        if in_src and in_tests:
            status = "COVERED"
        elif in_src or in_tests:
            status = "PARTIAL"
            gaps += 1
        else:
            status = "MISSING"
            gaps += 1
        lines.append(f"{tag} {status} src={src_hits.get(tag, [])} "
                     f"tests={test_hits.get(tag, [])}")
    orphans = sorted((set(src_hits) | set(test_hits)) - set(spec))
    for tag in orphans:
        lines.append(f"{tag} ORPHAN src={src_hits.get(tag, [])} "
                     f"tests={test_hits.get(tag, [])}")
    covered = len(spec) - gaps
    gap_word = "gap" if gaps == 1 else "gaps"
    orphan_word = "orphan" if len(orphans) == 1 else "orphans"
    lines.append(f"summary: {covered}/{len(spec)} covered, "
                 f"{gaps} {gap_word}, {len(orphans)} {orphan_word}")
    return lines, gaps


def default_spec():
    """REQ-010: default spec discovery under .kiro/specs/."""
    for dirpath, _, filenames in os.walk(".kiro/specs"):
        if "requirements.md" in filenames:
            return os.path.join(dirpath, "requirements.md")
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description="Kiro Spec Auditor")
    ap.add_argument("--spec", default=None)
    ap.add_argument("--src", default="src")
    ap.add_argument("--tests", default="tests")
    args = ap.parse_args(argv)
    spec_path = args.spec or default_spec()
    if not spec_path:
        print("error: no spec file found under .kiro/specs/", file=sys.stderr)
        return 2
    spec = parse_spec(spec_path)
    src_hits = scan_tree(args.src)
    test_hits = scan_tree(args.tests)
    lines, gaps = audit(spec, src_hits, test_hits)
    print("\n".join(lines))
    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main())
