# ✅ Smart Report Service — Fixed Dependencies

This folder (`issue_fixed/`) contains a secure, reproducible setup for the app. The original project was left untouched. All changes were made here.

## 🔧 Key Fixes
- **Pinned all dependencies** and aligned `requirements.txt` with `pyproject.toml`.
- **Python requirement** set to `>=3.10,<3.15` (works with the host Python 3.14.x).
- **Patched vulnerabilities**:
  - `PyYAML 5.4.1` ➜ `6.0.2` (fixes CVE-2020-14343 / GHSA-8q59-q68h-6hv4).
  - `httpx 0.23.0` ➜ `0.27.2` (addresses known GHSA advisories).
  - `jsonschema 3.2.0` ➜ `4.23.0` (adds Draft202012 support used in `config.py`).
- **Removed heavyweight compiled deps** (`pandas`, `numpy`) from mandatory requirements to avoid wheel/build failures on Python 3.14; code now has stdlib fallbacks.
  - Need them? Install optionally: `pip install pandas==2.2.3 numpy==1.26.4`.
- **Adopted pydantic v2** (2.12.5) + `pydantic-settings` (2.6.1); code paths remain backward-compatible with v1.
- Resolved resolver conflict by aligning **httpx==0.26.0** with **anyio==3.7.1** for FastAPI 0.104.x.
- Fixed **`app.models`** to expose `ReportRequest` for FastAPI.
- Added **automation scripts** and **auto_test.py** for consistent test runs.

## 🗂️ Layout
```
issue_fixed/
├─ app/
│  ├─ config.py, config.yaml, main.py, models.py, services.py, utils.py
├─ tests/
├─ requirements.txt
├─ requirements_backup.txt (original)
├─ pyproject.toml
├─ auto_test.py
├─ setup.sh / setup.bat
├─ run_test.sh / run_test.bat
├─ Dockerfile
├─ .gitignore
└─ report.json
```

## 🚀 Quickstart
```bash
cd issue_fixed
# Create & install deps
./setup.sh        # or: bash setup.sh
# Run tests (logs to logs/test_run.log)
./run_test.sh
```

**Windows (PowerShell/CMD)**
```bat
cd issue_fixed
setup.bat
run_test.bat
```

> 📁 A `.venv` folder will be created. It’s already ignored via `.gitignore`.

## 🧪 Auto Test Runner
- Script: `auto_test.py`
- Discovers and runs all tests in `tests/` using the `.venv` interpreter when present.
- Writes results to `logs/test_run.log` (auto-created).

## 🐳 Docker
```bash
docker build -t smart-report-service:latest .
docker run --rm -p 8000:8000 smart-report-service:latest
```
Browse: http://localhost:8000/health

## 🔐 Dependency Notes
- Pins match across `requirements.txt` and `pyproject.toml` to avoid drift.
- Consider generating hash-pinned locks with `pip-compile --generate-hashes` for production.
- Run `pip check` after installs; CI can enforce via `python -m pip check`.
- Pydantic v2 compatibility: avoid defining both `Config` and `model_config`; code uses version checks to stay compatible.

## ✅ Verification Checklist
- [x] `requirements_backup.txt` created from original
- [x] Dependencies pinned & upgraded
- [x] `.gitignore` updated to exclude `.venv`
- [x] `.venv` bootstrap scripts added
- [x] `report.json` documents the changes
- [x] `auto_test.py` logs to `logs/test_run.log`

## 📚 References
- PyYAML advisory: https://github.com/advisories/GHSA-8q59-q68h-6hv4
- FastAPI compatibility matrix: https://fastapi.tiangolo.com/

Happy testing! 🎉
