#!/usr/bin/env python
"""
Auto Test Runner
Discovers and runs all tests in the tests/ folder and logs results.
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime


def setup_logging():
    """Create logs directory if it doesn't exist"""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    return logs_dir


def get_test_results_log_path():
    """Get the path for test results log file"""
    logs_dir = Path("logs")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return logs_dir / f"test_run_{timestamp}.log"


def run_tests():
    """Run all tests and capture output"""
    log_path = get_test_results_log_path()
    
    print("=" * 70)
    print("Smart Report Service - Auto Test Runner")
    print("=" * 70)
    print(f"Python: {sys.version}")
    print(f"Working Directory: {os.getcwd()}")
    print(f"Log File: {log_path}")
    print("=" * 70)
    print()
    
    # Prepare pytest command
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "tests/",
        "-v",
        "--tb=short",
        "--color=yes",
    ]
    
    print(f"Running: {' '.join(cmd)}")
    print()
    
    # Run tests and capture output
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        # Write to log file
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("=" * 70 + "\n")
            f.write("Smart Report Service - Test Run Log\n")
            f.write("=" * 70 + "\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n")
            f.write(f"Python: {sys.version}\n")
            f.write(f"Command: {' '.join(cmd)}\n")
            f.write("=" * 70 + "\n\n")
            
            f.write("STDOUT:\n")
            f.write(result.stdout)
            f.write("\n\n")
            
            if result.stderr:
                f.write("STDERR:\n")
                f.write(result.stderr)
                f.write("\n\n")
            
            f.write("=" * 70 + "\n")
            f.write(f"Return Code: {result.returncode}\n")
            f.write(f"Status: {'PASSED' if result.returncode == 0 else 'FAILED'}\n")
            f.write("=" * 70 + "\n")
        
        # Print output
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        # Print summary
        print()
        print("=" * 70)
        print(f"Log saved to: {log_path}")
        status_text = "ALL TESTS PASSED" if result.returncode == 0 else "SOME TESTS FAILED"
        print(f"Status: {status_text}")
        print("=" * 70)
        
        return result.returncode
        
    except subprocess.TimeoutExpired:
        error_msg = "Tests timed out after 300 seconds"
        print(f"ERROR: {error_msg}")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(error_msg)
        return 1
    except Exception as e:
        error_msg = f"Error running tests: {str(e)}"
        print(f"ERROR: {error_msg}")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(error_msg)
        return 1


def main():
    """Main entry point"""
    setup_logging()
    exit_code = run_tests()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
