import sys
import subprocess
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_code_review():
    """Run the code review script."""
    subprocess.run(["python", os.path.join(SCRIPT_DIR, "codereview.py")])

def update_script():
    """Run the updater script."""
    subprocess.run(["python", os.path.join(SCRIPT_DIR, "updater.py")])

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
    else:
        print("❌ Unknown command. Use --help for options.")

if __name__ == "__main__":
    main()
