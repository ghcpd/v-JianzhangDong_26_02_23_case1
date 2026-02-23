#!/bin/bash
set -e

echo "================================"
echo "Smart Report Service Setup"
echo "================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
if [ ! -d ".venv" ]; then
    python -m venv .venv
    echo "Virtual environment created"
else
    echo "Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate
echo "Virtual environment activated"
echo ""

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip setuptools wheel
echo ""

# Install dependencies
echo "Installing dependencies from requirements.txt..."
python -m pip install -r requirements.txt
echo "Installation complete"
echo ""

# Verify installation
echo "Verifying installation..."
python -c "import fastapi; import pydantic; import pydantic_settings; print('All core dependencies verified')"
echo ""

echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "To activate the environment in the future, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To run tests, use:"
echo "  python auto_test.py"
echo ""
