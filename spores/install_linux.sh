#!/bin/bash
echo "🦠 AMOEBA SPORE — linux"
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:1b
echo "✓ Done. Return to AMOEBA and press CONNECT OLLAMA."
