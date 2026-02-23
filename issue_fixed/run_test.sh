#!/bin/bash
# run tests using the virtualenv's python
if [ -f ".venv/bin/python" ]; then
    .venv/bin/python auto_test.py
else
    echo "Virtual environment not found. Run setup.sh first." >&2
    exit 1
fi
