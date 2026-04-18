"""
PHYSIOLOGY / cortex.py
-----------------------
Signal routing intelligence.

Receives raw signals, classifies, routes to:
- metabolism  (actionable now)
- bureau      (pattern accumulation)
- immune      (dead function detection)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from physiology import metabolism, bureau, immune
from genome import soma

SIGNAL_TYPES = ["feedback", "mutation_request", "apoptosis_marker", "status"]

def receive(signal: dict) -> dict:
    """Entry point for all signals."""
    sig_type = signal.get("type", "unknown")
    if sig_type not in SIGNAL_TYPES:
        return {"error": f"Unknown signal type: {sig_type}"}

    bureau.accumulate(signal)

    if sig_type == "feedback":
        result = metabolism.metabolize(signal, soma.process_signal)
        return {"metabolism": result, "bureau": bureau.evaluate()}
    elif sig_type == "status":
        return soma.identity()
    elif sig_type == "apoptosis_marker":
        return immune.mark_for_apoptosis(signal.get("function"), signal.get("reason", "unspecified"))
    elif sig_type == "mutation_request":
        return bureau.evaluate()

    return {"routed": sig_type}
