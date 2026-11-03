#!/usr/bin/env python3
"""Run the test suite without pytest: executes every test_* function."""
import sys
import traceback

sys.path.insert(0, "tests")
import test_auditor

passed = failed = 0
for name in sorted(dir(test_auditor)):
    if not name.startswith("test_"):
        continue
    try:
        getattr(test_auditor, name)()
        print(f"PASS {name}")
        passed += 1
    except Exception:
        print(f"FAIL {name}")
        traceback.print_exc()
        failed += 1
print(f"{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
