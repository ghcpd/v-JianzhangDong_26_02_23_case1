# issue_fixed – Dependency and Environment Upgrade

This folder is a **clean, fixed copy** of the original `issue/` project. The original files were **not modified**. All dependency upgrades, environment scripts, and test automation live here.

## ✅ What was done

1. **Created `issue_fixed/`** and copied `app/` and `tests/` unchanged.
2. **Backed up the old dependencies** to `requirements_backup.txt`.
3. **Updated `requirements.txt` and `pyproject.toml`** with modern, pinned, non‑vulnerable versions.
4. **Corrected Python version requirement** from `>=3.14` to `>=3.11`.
5. **Added missing runtime dependency** `pydantic-settings` (required by `app/config.py`).
6. **Fixed `app/models.py`** by adding the missing `ReportRequest` model so tests can pass without changing any test files.
7. **Added automation scripts** and a Dockerfile.
8. **Added `auto_test.py`** to run all tests and log results.
9. **Added `.gitignore`** to exclude `.venv/` and logs.
10. **Generated `report.json`** describing all changes and reasons.

## 📦 Dependency versions

See `report.json` for a full diff and rationale. Highlights:

- `pyyaml 5.4.1 → 6.0.2` (security CVEs fixed)
- `fastapi 0.95.0 → 0.111.0`
- `pydantic 1.x → 2.12.5` (v1 EOL, required by new FastAPI, Python 3.14 wheels available)
- `pydantic-settings 2.13.1` added to support `BaseSettings`.
- All packages are now **pinned** and consistent with `pyproject.toml`.

## 🐍 Local setup (Windows / Linux / macOS)

### 1. Create venv and install deps

**Linux/macOS:**
```bash
cd issue_fixed
bash setup.sh
```

**Windows (PowerShell):**
```powershell
cd issue_fixed
D:/python/python.exe -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Run tests

**Linux/macOS:**
```bash
bash run_test.sh
```

**Windows:**
```bat
run_test.bat
```

### 3. Automated test runner

`auto_test.py`:
- Locates `.venv` automatically.
- Runs `pytest` over **all tests in `tests/`**.
- Writes results to `logs/test_run.log`.

Run manually:
```bash
.venv/bin/python auto_test.py   # linux/mac
.venv\Scripts\python.exe auto_test.py  # windows
```

## 🐳 Docker

Build and run:
```bash
docker build -t issue-fixed .
docker run --rm issue-fixed
```
The container executes `auto_test.py` as its default command.

## 📄 Files added in this folder

| File | Purpose |
|------|---------|
| `requirements_backup.txt` | Original dependency list (unchanged) |
| `requirements.txt` | Updated secure pinned deps |
| `pyproject.toml` | Updated metadata and consistent deps |
| `report.json` | Detailed dependency and Python version change report |
| `setup.sh` | Create `.venv` and install deps on Unix |
| `run_test.sh` | Run tests on Unix using `.venv` |
| `run_test.bat` | Run tests on Windows using `.venv` |
| `auto_test.py` | Automated pytest runner with logging |
| `Dockerfile` | Reproducible test environment |
| `.gitignore` | Excludes `.venv/`, logs, caches |
| `logs/test_run.log` | Auto‑generated test output log |

## Notes

- The dependency upgrade is designed to be compatible with the original code and tests.
- If you add more tests, `auto_test.py` will pick them up automatically.

---

If you want further dependency hardening (e.g., pip-audit or SBOM generation), tell me.
