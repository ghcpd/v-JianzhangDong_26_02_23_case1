#!/bin/bash
# Create a virtual environment and install dependencies
python -m venv .venv

# Activate (for POSIX shells)
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Environment setup complete. Use '.venv/bin/activate' or '.venv\Scripts\activate' on Windows."