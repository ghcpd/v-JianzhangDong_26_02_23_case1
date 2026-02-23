@echo off
REM run tests using the virtualenv's python
IF EXIST ".venv\Scripts\python.exe" (
    .venv\Scripts\python.exe auto_test.py
) ELSE (
    echo Virtual environment not found. Run setup.sh first.
    exit /b 1
)
