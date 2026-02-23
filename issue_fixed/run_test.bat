@echo off
setlocal enabledelayedexpansion

echo Running tests...
call .venv\Scripts\activate.bat
python -m pytest tests/ -v --tb=short
