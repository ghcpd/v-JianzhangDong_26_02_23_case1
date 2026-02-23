@echo off
REM Test runner for Windows environments
REM Runs all tests using the virtual environment

echo === Smart Report Service - Running Tests ===
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run the setup first by creating a virtual environment.
    echo.
    echo Run these commands:
    echo   python -m venv .venv
    echo   .venv\Scripts\activate
    echo   pip install -r requirements.txt
    echo.
    exit /b 1
)

REM Activate virtual environment and run tests
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Running tests...
python auto_test.py

echo.
echo Tests complete! Check logs/test_run.log for detailed results.
echo.

pause
