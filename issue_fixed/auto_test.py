import os
import subprocess
import sys
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "test_run.log")

if not os.path.isdir(LOG_DIR):
    os.makedirs(LOG_DIR)

# determine path to the python executable inside the venv
base = os.path.abspath(os.getcwd())
if os.name == "nt":
    python_bin = os.path.join(base, ".venv", "Scripts", "python.exe")
else:
    python_bin = os.path.join(base, ".venv", "bin", "python")

if not os.path.isfile(python_bin):
    print("Virtual environment not found, please run setup.sh or create .venv first.")
    sys.exit(1)

cmd = [python_bin, "-m", "pytest", "tests"]

with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write(f"\n===== Test run at {datetime.utcnow().isoformat()}Z =====\n")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        f.write(line)
        print(line, end="")
    ret = process.wait()
    f.write(f"\nexit code: {ret}\n")

sys.exit(ret)
