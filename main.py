import sys
import subprocess
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_CMD = "python3"

def run_code_review():
    """Run the code review script."""
    subprocess.run([PYTHON_CMD, os.path.join(SCRIPT_DIR, "git_review.py")])

def update_script():
    """Run the update script."""
    subprocess.run([PYTHON_CMD, os.path.join(SCRIPT_DIR, "update.py")])

def uninstall_script():
    """Run the uninstaller script."""
    subprocess.run([PYTHON_CMD, os.path.join(SCRIPT_DIR, "uninstall.py")])

def show_help():
    """Display help message."""
    print("""
Usage: git_review.py [OPTION]

Options:
  --review    Run the AI-powered code review.
  --update    Update the script to the latest version.
  --help      Show this help message.
""")

def main():
    try:
        if len(sys.argv) < 2:
            show_help()
            return

        command = sys.argv[1]

        if command == "--review":
            run_code_review()
        elif command == "--update":
            update_script()
        elif command == "--help":
            show_help()
        elif command.startswith("--uninstall"):
            uninstall_script()
        else:
            print("❌ Unknown command. Use --help for options.")
    except KeyboardInterrupt:
        print("❌ Operation cancelled.")

if __name__ == "__main__":
    main()
