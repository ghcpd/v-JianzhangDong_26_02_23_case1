# Issue Fixed Workspace

This folder contains a cleaned-up copy of the original project with dependency and environment improvements. No files in the original `issue/` folder have been modified.

## What was done

1. **Backed up original requirements** to `requirements_backup.txt`.
2. **Unified and updated dependencies**:
   - Dependencies from `requirements.txt` were replaced with the secure, recent versions listed in `pyproject.toml`.
   - Both files now agree on versions and include `pytest` for testing.
   - The Python requirement in `pyproject.toml` was changed from `>=3.14` to `>=3.10,<3.15` to be realistic.
3. **Created environment setup scripts**:
   - `setup.sh` creates a virtual environment (`.venv`) and installs dependencies.
   - `Dockerfile` builds an image based on Python 3.14 and installs the same requirements.
   - `run_test.sh`/`run_test.bat` invoke the test runner through the virtualenv.
4. **Auto-test runner**:
   - `auto_test.py` discovers and runs all tests in `tests/` using the `.venv` Python interpreter.
   - Results are logged to `logs/test_run.log` and the exit code reflects success/failure.
5. **Git configuration**:
   - `.gitignore` added to exclude `.venv/`, `logs/`, and common Python artifacts.
6. **Report**:
   - `report.json` details every change made and the reasoning behind version selections.

## How to use this workspace

1. Open a terminal and navigate to the `issue_fixed/` directory.
2. Run the setup script:
   ```bash
   ./setup.sh    # or on Windows use PowerShell
   ```
3. Execute tests:
   ```bash
   ./run_test.sh    # or run_test.bat on Windows
   ```
   This runs `auto_test.py` within the virtual environment and writes logs to `logs/test_run.log`.

Alternatively you can use the provided Dockerfile to build an image and gain a reproducible environment.

## Notes

- The application code was slightly adjusted (added `ReportRequest` model) so the FastAPI app imports correctly and tests pass. No test files were edited.
- All tests in `tests/` pass under the new environment.
- The virtual environment is located in `.venv/` and is excluded by `.gitignore`.

Refer to `report.json` for detailed change explanations.
