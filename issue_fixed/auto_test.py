import os
import sys
import subprocess
from pathlib import Path

def get_venv_python():
    # if running inside venv, just return current
    if hasattr(sys, "real_prefix") or sys.prefix != sys.base_prefix:
        return sys.executable
    base = Path(__file__).parent
    if os.name == "nt":
        return str(base / ".venv" / "Scripts" / "python.exe")
    else:
        return str(base / ".venv" / "bin" / "python")


def main():
    python_exe = get_venv_python()
    if not os.path.exists(python_exe):
        print("Virtual environment python not found. Please run setup.sh first.")
        sys.exit(1)
    # ensure logs directory
    logpath = Path("logs")
    logpath.mkdir(exist_ok=True)
    logfile = logpath / "test_run.log"
    # run pytest
    proc = subprocess.run([python_exe, "-m", "pytest", "tests"], capture_output=True, text=True)
    with open(logfile, "w", encoding="utf-8") as f:
        f.write(proc.stdout)
        f.write(proc.stderr)
    print(f"Tests finished with exit code {proc.returncode}, see {logfile}")
    sys.exit(proc.returncode)

if __name__ == "__main__":
    main()
