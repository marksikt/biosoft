"""
PHYSIOLOGY / bureau.py
-----------------------
The Bureau of Evolution.

Accumulates signals. At threshold, proposes genome mutation.
Does not act on noise. Requires pattern before proposing change.
Cannot touch the nucleus (GENOME_VERSION, NUCLEUS_CHECKSUM).
"""

import json
from pathlib import Path
from collections import Counter

SIGNALS_DIR = Path(__file__).parent.parent / "signals"
THRESHOLD = 3

def accumulate(signal: dict):
    """Log a signal for pattern analysis."""
    with open(SIGNALS_DIR / "bureau_log.jsonl", "a") as f:
        f.write(json.dumps(signal) + "\n")

def evaluate() -> dict:
    """Check if any signal pattern has crossed mutation threshold."""
    log = SIGNALS_DIR / "bureau_log.jsonl"
    if not log.exists():
        return {"mutation_proposed": False}
    signals = []
    with open(log) as f:
        for line in f:
            try:
                signals.append(json.loads(line))
            except Exception:
                pass
    types = Counter(s.get("type", "unknown") for s in signals)
    for sig_type, count in types.items():
        if count >= THRESHOLD:
            return {
                "mutation_proposed": True,
                "signal_type": sig_type,
                "count": count,
                "recommendation": f"Genome adaptation needed for: {sig_type}"
            }
    return {"mutation_proposed": False, "signal_counts": dict(types)}
