#!/bin/bash
DIR="$(dirname "$0")"
source "$DIR/venv/bin/activate"
python3 "$DIR/quantum_logger.py"
