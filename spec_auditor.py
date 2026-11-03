#!/usr/bin/env python3
"""Thin entry point; real implementation lives in src/spec_auditor.py."""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from spec_auditor import main
if __name__ == "__main__":
    sys.exit(main())
