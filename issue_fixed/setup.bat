@echo off
setlocal enabledelayedexpansion
set ROOT_DIR=%~dp0
cd /d %ROOT_DIR%

set PYTHON_BIN=%PYTHON_BIN%
if "%PYTHON_BIN%"=="" set PYTHON_BIN=python

if not exist .venv (
  echo [setup] Creating virtual environment...
  %PYTHON_BIN% -m venv .venv
) else (
  echo [setup] .venv already exists
)

set PYTHON_EXE=.venv\Scripts\python.exe
"%PYTHON_EXE%" -m pip install --upgrade pip wheel setuptools
"%PYTHON_EXE%" -m pip install -r requirements.txt

echo [setup] Done. To activate: call .venv\Scripts\activate.bat
endlocal
