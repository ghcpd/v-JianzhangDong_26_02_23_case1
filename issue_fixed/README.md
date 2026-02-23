# Issue Fixed Project

This directory is a sanitized and upgraded copy of the original `issue/` project. It demonstrates how to resolve outdated dependencies, enforce reproducible environments, and provide accompanying tooling to run tests smoothly.

## What's Included

- **requirements_backup.txt** – original dependency pins preserved for reference.
- **requirements.txt** – updated, secure, and fully pinned packages; aligned with `pyproject.toml`.
- **report.json** – documents the changes made to dependency versions along with reasons.
- **.gitignore** – ignores the virtual environment, logs, and cache files.
- **Dockerfile** – builds a containerized environment with the application installed.
- **setup.sh** – shell script to create a virtual environment (`.venv`) and install dependencies.
- **run_test.sh / run_test.bat** – wrapper scripts to execute `auto_test.py` on Unix/Windows.
- **auto_test.py** – script that discovers and runs all tests under `tests/` using the `.venv` Python and writes output to `logs/test_run.log`.
- **Logs directory** – created at runtime to capture test outputs.

All original application code (`app/`) and tests (`tests/`) are present unmodified.

## Dependency Upgrades

Outdated or insecure packages such as `pyyaml 5.4.1` were upgraded to safe releases. The Python version requirement in `pyproject.toml` has been normalized to `>=3.11, <3.15` and dependencies have been aligned with `requirements.txt`. The current build environment uses Python 3.14.2, but the project itself targets any Python 3.11–3.14 runtime.

The `report.json` contains a detailed changelog of package versions.

## Using the Project

### Local Setup

1. Open a terminal in this directory.
2. Run `./setup.sh` (or `python -m venv .venv && .venv\Scripts\activate \n pip install -r requirements.txt` on Windows) to prepare the environment.
3. Activate the virtual environment:
   - Unix/macOS: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
4. Run tests manually:
   ```bash
   python -m pytest tests
   ```
   Or use the helper scripts below.

### Running Tests via Provided Scripts

- **Shell**: `./run_test.sh`
- **Batch**: `run_test.bat` (Windows cmd)

Each invocation appends results to `logs/test_run.log` and returns a non-zero status if any test fails.

### Docker

Build and run inside Docker:

```sh
docker build -t issue-fixed .
docker run --rm -p 8000:8000 issue-fixed
```

This will start the FastAPI service on port 8000.

## Notes

- The tests currently exercise basic functionality (health endpoint, summary generation, ISO date parsing) and pass under the upgraded dependencies.
- No modifications were made to the test files themselves as per the requirement.

Feel free to explore, extend, or use this setup as a template for maintaining secure Python projects.
