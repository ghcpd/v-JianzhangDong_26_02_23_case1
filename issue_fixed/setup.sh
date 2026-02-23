#!/bin/bash

# Setup script for Linux/Mac environments
# Creates virtual environment and installs dependencies

set -e

echo "=== Smart Report Service - Environment Setup ==="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

# Create virtual environment
echo ""
echo "Creating virtual environment in .venv/..."
python3 -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Create logs directory
echo ""
echo "Creating logs directory..."
mkdir -p logs

echo ""
echo "=== Setup Complete ==="
echo ""
echo "To activate the virtual environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To run tests, use:"
echo "  python auto_test.py"
echo "  or"
echo "  ./run_test.sh"
echo ""
