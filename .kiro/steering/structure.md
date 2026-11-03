# Steering — Kiro Spec Auditor

- One requirement = one `REQ-XXX` tag, one verifiable statement. No vague
  requirements ("should be fast", "should be good").
- A status word means exactly what design.md says: COVERED is a reference
  in code AND tests, never a claim that the feature works.
- Never silently pass: gaps exit non-zero, orphans are listed, errors are
  printed instead of an empty report.
- Stdlib only, no network, no new dependencies without a reason written here.
- Keep the tool honest in the submission too: demo output must be real
  runs, not hand-written.
