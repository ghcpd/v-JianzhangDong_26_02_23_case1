@echo off
setlocal
cd /d %~dp0

if not exist .venv\Scripts\python.exe (
  echo No .venv found. Run setup.sh or create it manually.
  exit /b 1
)

.venv\Scripts\python.exe auto_test.py
endlocal
