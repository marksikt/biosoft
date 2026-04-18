# SIGNALS

Input interface. Accepts external feedback and internal state reports.

Signal format (JSONL):
{"type": "feedback",          "content": "...", "source": "external"}
{"type": "mutation_request",  "target": "fn_name"}
{"type": "apoptosis_marker",  "function": "fn_name", "reason": "unused"}
{"type": "status"}
