#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$ROOT_DIR"

PYTHON_BIN="${PYTHON_BIN:-python3}"

# Create virtual environment
if [ ! -d .venv ]; then
  echo "[setup] Creating virtual environment..."
  "$PYTHON_BIN" -m venv .venv
fi

# Activate and upgrade pip
source .venv/bin/activate
python -m pip install --upgrade pip wheel setuptools

# Install dependencies
python -m pip install -r requirements.txt

echo "[setup] Done. To activate: source .venv/bin/activate"
