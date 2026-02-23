@echo off
setlocal enabledelayedexpansion

echo ================================
echo Smart Report Service Setup
echo ================================
echo.

REM Check Python version
echo Checking Python version...
python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist ".venv" (
    python -m venv .venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat
echo Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip setuptools wheel
echo.

REM Install dependencies
echo Installing dependencies from requirements.txt...
python -m pip install -r requirements.txt
echo Installation complete
echo.

REM Verify installation
echo Verifying installation...
python -c "import fastapi; import pydantic; import pydantic_settings; print('All core dependencies verified')"
echo.

echo ================================
echo Setup Complete!
echo ================================
echo.
echo To activate the environment in the future, run:
echo   .venv\Scripts\activate.bat
echo.
echo To run tests, use:
echo   python auto_test.py
echo.
