import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime, UTC

ROOT = Path(__file__).parent
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "test_run.log"


def _find_venv_python() -> Path:
    """Return the python executable inside .venv for this platform."""
    venv_dir = ROOT / ".venv"
    if os.name == "nt":
        candidate = venv_dir / "Scripts" / "python.exe"
    else:
        candidate = venv_dir / "bin" / "python"
    return candidate


def main() -> int:
    venv_python = _find_venv_python()

    with LOG_FILE.open("a", encoding="utf-8") as log:
        log.write("=" * 80 + "\n")
        log.write(f"Test run at {datetime.now(UTC).isoformat()}\n")

        if not venv_python.exists():
            msg = f"ERROR: virtual environment not found at {venv_python}. Create it first.\n"
            log.write(msg)
            print(msg, file=sys.stderr)
            return 1

        cmd = [str(venv_python), "-m", "pytest", "tests", "-q"]
        log.write(f"Running: {' '.join(cmd)}\n")

        proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)

        log.write("--- stdout ---\n")
        log.write(proc.stdout + "\n")
        log.write("--- stderr ---\n")
        log.write(proc.stderr + "\n")
        log.write(f"Exit code: {proc.returncode}\n")

    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
    else:
        print("All tests passed. See logs/test_run.log for details.")

    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
