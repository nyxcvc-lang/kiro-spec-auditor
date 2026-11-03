# Kiro Spec Auditor — Kiroween 2026

**Idea:** a spec is only useful if the code actually follows it. This tool checks that every `REQ-XXX` in a Kiro `requirements.md` must be referenced by source code AND by tests. Anything else is reported as a gap.

**Status:** working scaffold + self-auditing demo. Built with Kiro-style specs (requirements / design / tasks under `.kiro/`).

## What it does

```
$ python3 spec_auditor.py --spec .kiro/specs/spec-auditor/requirements.md \
  --src src --tests tests
REQ-001 COVERED src=['src/spec_auditor.py'] tests=['tests/test_auditor.py']
...
summary: 10/10 covered, 0 gaps, 1 orphans
```

- `COVERED` — tag in source and tests. `PARTIAL` — in one only. `MISSING` — in neither. `ORPHAN` — tag in code/tests, not in the spec.
- Exit codes: 0 = all covered, 1 = gaps, 2 = usage/spec error.
- Stdlib only, no network, language-agnostic (plain text search).

**Honest limit, stated on purpose:** a tag match proves a requirement is *referenced*, not that the feature works. Test execution stays in CI. The demo report (`demo-report.txt`) is real output from the self-audit run, not hand-written. `REQ-999` in the report is a deliberate orphan fixture in the test file, included to show orphan detection working.

## Layout

```
.kiro/specs/spec-auditor/requirements.md  # REQ-001..REQ-010
.kiro/specs/spec-auditor/design.md
.kiro/specs/spec-auditor/tasks.md
.kiro/steering/structure.md
src/spec_auditor.py          # the checker
spec_auditor.py              # thin entry point
tests/test_auditor.py        # pytest-style tests
demo-report.txt              # real self-audit output
```

## Run it

```bash
python3 spec_auditor.py --spec <requirements.md> --src <src-dir> --tests <test-dir>
# no arguments: audits .kiro/specs/ against src/ and tests/
python3 spec_auditor.py
```

## Status

Working scaffold with a self-auditing example. See Run it above to audit a spec.
