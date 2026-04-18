"""
PHYSIOLOGY / metabolism.py
--------------------------
Input -> Process -> Output + Waste

The metabolism loop. Signals come in, processed by genome functions,
output returned, deprecated matter excreted to waste/.
"""

import json
import datetime
from pathlib import Path

WASTE_DIR = Path(__file__).parent.parent / "waste"
WASTE_DIR.mkdir(exist_ok=True)

def metabolize(signal: dict, genome_fn) -> dict:
    """Run signal through genome function. Excrete waste if needed."""
    result = genome_fn(signal)
    if result.get("waste"):
        _excrete(result["waste"])
        result["waste"] = "excreted"
    return result

def _excrete(content):
    """Write deprecated matter to waste log."""
    timestamp = datetime.datetime.utcnow().isoformat()
    entry = {"timestamp": timestamp, "content": content}
    with open(WASTE_DIR / "waste.log", "a") as f:
        f.write(json.dumps(entry) + "\n")
