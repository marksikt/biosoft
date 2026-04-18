"""
PHYSIOLOGY / immune.py
-----------------------
Dead function detection -> Apoptosis.

Monitors genome for disuse or corruption.
Marks functions for excretion. Does not delete.
"""

import ast
import json
import datetime
from pathlib import Path

GENOME_FILE = Path(__file__).parent.parent / "genome" / "soma.py"
WASTE_DIR = Path(__file__).parent.parent / "waste"

def scan_genome() -> list:
    """Return list of active function names in soma.py."""
    tree = ast.parse(GENOME_FILE.read_text())
    return [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]

def mark_for_apoptosis(fn_name: str, reason: str):
    """Record a function as candidate for excretion."""
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "function": fn_name,
        "reason": reason,
        "status": "marked"
    }
    with open(WASTE_DIR / "apoptosis.log", "a") as f:
        f.write(json.dumps(entry) + "\n")
    return entry
