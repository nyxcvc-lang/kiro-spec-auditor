# Requirements — Kiro Spec Auditor

## Introduction
Kiro Spec Auditor checks whether an implementation actually follows its Kiro
spec: every requirement in `requirements.md` must be traceable to code and to
at least one test. Uncovered requirements are reported, not silently passed.

## Glossary
- **Requirement**: one verifiable statement, tagged `REQ-XXX`.
- **Coverage**: a requirement is COVERED when its tag appears in source code
  and in at least one test file.
- **Orphan**: a requirement tag that appears in code/tests but not in the spec.

## Requirements

### Requirement 1: Parse a spec file
**User Story:** As a developer, I want the auditor to read my requirements file,
so that I get a complete list of what must be covered.

#### Acceptance Criteria
- REQ-001: WHEN given a Markdown spec file, THE auditor SHALL extract every
  `REQ-\d+` tag with its one-line statement.
- REQ-002: WHEN the spec file is missing or unreadable, THE auditor SHALL exit
  non-zero with a clear error message, not an empty report.

### Requirement 2: Trace requirements to code and tests
**User Story:** As a developer, I want to see which requirements have code and
tests behind them, so that gaps are visible before submission.

#### Acceptance Criteria
- REQ-003: WHEN scanning source directories, THE auditor SHALL record every
  requirement tag referenced in source files.
- REQ-004: WHEN scanning test directories, THE auditor SHALL record every
  requirement tag referenced in test files.
- REQ-005: WHEN a requirement appears in source but not in tests (or vice
  versa), THE auditor SHALL mark it PARTIAL, not COVERED.

### Requirement 3: Report gaps plainly
**User Story:** As a developer, I want a short report I can act on, so that I
fix gaps instead of reading a wall of text.

#### Acceptance Criteria
- REQ-006: WHEN the audit finishes, THE auditor SHALL print one line per
  requirement: id, status (COVERED / PARTIAL / MISSING), and where found.
- REQ-007: WHEN any requirement is MISSING or PARTIAL, THE auditor SHALL exit
  non-zero; WHEN all are COVERED, THE auditor SHALL exit zero.
- REQ-008: WHEN a tag appears in code/tests but not in the spec, THE auditor
  SHALL list it as ORPHAN, separately from requirement statuses.

### Requirement 4: Stay language-agnostic
**User Story:** As a developer, I want the auditor to work on any repo, so that
it is not tied to one language's test framework.

#### Acceptance Criteria
- REQ-009: WHEN scanning, THE auditor SHALL treat files as text and match tags
  by plain string search, with no language-specific parsing.
- REQ-010: WHEN run with no arguments, THE auditor SHALL audit the current
  directory's `.kiro/specs/` tree against `src/` and `tests/` by default.
