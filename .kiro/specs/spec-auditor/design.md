# Design — Kiro Spec Auditor

## Overview
A single-file, dependency-free checker (Python 3, stdlib only). It does three
passes over plain text and prints a gap report. No network, no language
parsers, no test-framework integration — that keeps it honest: it proves a
requirement is *referenced* by code and tests, not that the tests pass.
Test execution itself stays the developer's job (CI runs the suite).

## Architecture
```
spec-auditor.py
  ├── parse_spec(path)      -> {REQ-001: "statement", ...}
  ├── scan_tree(root)       -> {tag: [files]}
  └── report(spec, src, tests) -> lines + exit code
```

## Components
- **Parser**: regex `REQ-\d+` over the spec Markdown; the statement is the
  rest of the line the tag appears on, trimmed.
- **Scanner**: recursive walk of a directory tree, skipping hidden dirs
  (`.git`, `.kiro` itself is scanned only when explicitly given as spec),
  binary files, and files over 1 MB. Plain substring search per tag.
- **Reporter**: one line per requirement, `REQ-XXX STATUS [src files] [test
  files]`, then an ORPHAN section, then a one-line summary count.

## Statuses
- COVERED: tag in >= 1 source file AND >= 1 test file.
- PARTIAL: tag in source XOR tests.
- MISSING: tag in neither.
- ORPHAN: tag in code/tests but absent from the spec.

## Correctness notes
- A tag match is a reference, not a proof of implementation. The report says
  "referenced", and the README says so too — no overclaiming.
- Exit codes: 0 = all covered, 1 = any gap, 2 = usage/spec error.

## Testing strategy
- Self-audit: the auditor's own spec (this directory) is audited against
  its own source and tests, so the demo report is real output.
- Unit tests cover: tag parsing, missing-spec error, partial vs covered,
  orphan listing, and exit codes.
