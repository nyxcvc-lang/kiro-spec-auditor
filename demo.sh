#!/bin/bash
# 60-second demo script: self-audit (green) then example gap (red).
set -e
echo "=== 1. Self-audit: all requirements covered ==="
python3 spec_auditor.py --spec .kiro/specs/spec-auditor/requirements.md --src src --tests tests
echo
echo "=== 2. Example project: one requirement missing ==="
python3 spec_auditor.py --spec example/requirements.md --src example/src --tests example/tests || echo "(exit 1 = gaps found, as designed)"
