@echo off
setlocal enabledelayedexpansion
set ROOT_DIR=%~dp0
cd /d %ROOT_DIR%

if not exist .venv (
  echo [run_test] .venv not found. Run setup.bat or setup.sh first.
  exit /b 1
)

set PYTHON_EXE=.venv\Scripts\python.exe
"%PYTHON_EXE%" auto_test.py
endlocal
