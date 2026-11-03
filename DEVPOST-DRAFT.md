# Devpost draft — Kiro Spec Auditor (NOT submitted, text only)

## Title
Kiro Spec Auditor — prove your code actually follows your spec

## Tagline
Every requirement in your Kiro spec, traced to code and tests — or reported
as a gap. No silent passes.

## Description
Kiro specs are great at describing what to build. They are silent about
whether the build kept its promises. Spec Auditor closes that loop: it
reads `requirements.md`, finds every `REQ-XXX`, and checks that each one is
referenced by source code AND by tests.

- COVERED / PARTIAL / MISSING / ORPHAN, one line per requirement.
- Exit 0 when everything is covered, 1 when there are gaps, 2 on usage errors.
- Stdlib-only Python, no network, language-agnostic (plain text search).
- Self-auditing: the tool's own spec is audited by the tool (10/10 covered).

Honest limit, stated in the README: a tag match proves a requirement is
referenced, not that the feature works. Test execution stays in CI.

## How it was built with Kiro
Requirements, design, and tasks live under `.kiro/specs/spec-auditor/`;
steering rules under `.kiro/steering/`. The implementation follows the
tasks file in order, and the demo is real terminal output (`demo.sh`,
`demo-output.txt`), not hand-written.

## Demo
Run `./demo.sh`: first the self-audit (all green), then an example
calculator project with one deliberately missing requirement (REQ-103),
reported MISSING with exit 1.

## Links (fill in before submitting)
- Repo: <paste GitHub URL here>
- Demo video: <paste link here>

## Deadlines (from Devpost emails, Asia/Singapore)
- Free Kiro credits (4,000) request: 2 Dec 2026 04:00 +08, Resources tab.
- Final submission: 5 Dec 2026 06:00 +08.
- Repo must include a `/.kiro` directory at root.
