@echo off
REM activate and run tests on Windows
python -m venv .venv
.venv\Scripts\activate
python auto_test.py
