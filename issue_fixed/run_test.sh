#!/bin/bash

# Test runner for Linux/Mac environments
# Runs all tests using the virtual environment

set -e

echo "=== Smart Report Service - Running Tests ==="
echo ""

# Check if virtual environment exists
if [ ! -f ".venv/bin/activate" ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please run ./setup.sh first to create the environment."
    echo ""
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Run tests
echo ""
echo "Running tests..."
python auto_test.py

echo ""
echo "Tests complete! Check logs/test_run.log for detailed results."
echo ""
