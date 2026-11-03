# Implementation Plan — Kiro Spec Auditor

- [x] 1. Spec parser
  - Extract `REQ-\d+` tags + statements from Markdown.
  - Error clearly on missing/unreadable spec file.
  - _Requirements: REQ-001, REQ-002_

- [x] 2. Tree scanner
  - Recursive text scan with binary/oversize skips.
  - Separate source hits from test hits.
  - _Requirements: REQ-003, REQ-004, REQ-009_

- [x] 3. Reporter + exit codes
  - One line per requirement with status and file hits.
  - ORPHAN section for tags outside the spec.
  - Exit 0 / 1 / 2 semantics.
  - _Requirements: REQ-005, REQ-006, REQ-007, REQ-008_

- [x] 4. Defaults + CLI
  - No-arg run audits `.kiro/specs/` vs `src/` + `tests/`.
  - Flags: `--spec`, `--src`, `--tests`.
  - _Requirements: REQ-010_

- [x] 5. Demo + submission polish
  - Self-audit output saved as `demo-report.txt`.
  - Demo script `demo.sh` + `demo-output.txt` (self-audit green, example gap red) + `example/` target project with a deliberate REQ-103 gap.
  - Terminal demo recording `demo.cast` (from `script -c ./demo.sh`).
  - Tests runnable without pytest: `python3 run_tests.py` (4/4 pass).
  - Repo is public.
  - Remaining: hosted demo video link, Devpost Additional info step, request free credits by 2 Dec 2026 04:00 +08, final submit by 5 Dec 2026 06:00 +08.
  - _Requirements: all (demonstration)_
