#!/usr/bin/env python3
"""
Automated Test Runner for Smart Report Service
Discovers and runs all tests in the tests/ folder using pytest
Logs results to logs/test_run.log
"""

import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime


def ensure_venv_active():
    """Check if we're running in the virtual environment"""
    venv_path = Path(".venv")
    
    if sys.platform == "win32":
        venv_python = venv_path / "Scripts" / "python.exe"
    else:
        venv_python = venv_path / "bin" / "python"
    
    # Check if venv exists
    if not venv_python.exists():
        print("ERROR: Virtual environment not found at .venv/")
        print("Please create it first:")
        print("  python -m venv .venv")
        print("  .venv/Scripts/activate  (Windows)")
        print("  source .venv/bin/activate  (Linux/Mac)")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    
    # If not running from venv, restart with venv python
    current_python = Path(sys.executable)
    if current_python.resolve() != venv_python.resolve():
        print(f"Restarting with virtual environment Python: {venv_python}")
        result = subprocess.run(
            [str(venv_python), __file__],
            cwd=os.getcwd()
        )
        sys.exit(result.returncode)


def setup_logging():
    """Ensure logs directory exists"""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    return logs_dir / "test_run.log"


def run_tests(log_file):
    """Run pytest and capture output to log file"""
    print("=" * 70)
    print("Smart Report Service - Automated Test Runner")
    print("=" * 70)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python: {sys.version}")
    print(f"Working Directory: {os.getcwd()}")
    print(f"Log File: {log_file}")
    print("=" * 70)
    print()
    
    # Set PYTHONPATH to include current directory
    env = os.environ.copy()
    env['PYTHONPATH'] = os.getcwd()
    
    # Run pytest with verbose output
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",           # Verbose output
        "--tb=short",   # Short traceback format
        "-ra",          # Show summary of all test outcomes
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    print()
    
    # Run tests and capture output
    with open(log_file, 'w', encoding='utf-8') as f:
        # Write header to log
        f.write("=" * 70 + "\n")
        f.write("Smart Report Service - Test Run Log\n")
        f.write("=" * 70 + "\n")
        f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Python: {sys.version}\n")
        f.write(f"Working Directory: {os.getcwd()}\n")
        f.write("=" * 70 + "\n\n")
        f.flush()
        
        # Run pytest with output to both console and log file
        result = subprocess.run(
            cmd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Write output to log and print to console
        output = result.output if hasattr(result, 'output') else result.stdout
        print(output)
        f.write(output)
        f.write("\n" + "=" * 70 + "\n")
        f.write(f"Test run completed with exit code: {result.returncode}\n")
        
        if result.returncode == 0:
            f.write("Status: ALL TESTS PASSED ✓\n")
        else:
            f.write("Status: SOME TESTS FAILED ✗\n")
        
        f.write("=" * 70 + "\n")
    
    print()
    print("=" * 70)
    if result.returncode == 0:
        print("✓ ALL TESTS PASSED")
    else:
        print("✗ SOME TESTS FAILED")
    print(f"Detailed results saved to: {log_file}")
    print("=" * 70)
    
    return result.returncode


def main():
    """Main entry point"""
    # Ensure we're using venv
    ensure_venv_active()
    
    # Setup logging
    log_file = setup_logging()
    
    # Run tests
    exit_code = run_tests(log_file)
    
    # Exit with pytest's exit code
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
