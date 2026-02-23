import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "test_run.log"


def find_venv_python() -> Path:
    """Locate the virtual environment's python executable."""

    candidates = [
        ROOT / ".venv" / "Scripts" / "python.exe",  # Windows
        ROOT / ".venv" / "bin" / "python",  # POSIX
    ]
    for cand in candidates:
        if cand.exists():
            return cand
    return Path(sys.executable)


def run_pytest(python_exe: Path) -> int:
    env = os.environ.copy()
    env.setdefault("PYTHONPATH", str(ROOT))
    cmd = [str(python_exe), "-m", "pytest", "-q", "tests"]
    from datetime import timezone

    with LOG_FILE.open("a", encoding="utf-8") as log:
        log.write(f"\n=== Test run at {datetime.now(timezone.utc).isoformat()} ===\n")
        log.write(f"Command: {' '.join(cmd)}\n")
        process = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=log, stderr=log)
        process.wait()
        log.write(f"Exit code: {process.returncode}\n")
    return process.returncode


def main() -> int:
    python_exe = find_venv_python()
    return run_pytest(python_exe)


if __name__ == "__main__":
    sys.exit(main())
