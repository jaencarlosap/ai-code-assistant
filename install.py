import os
import shutil
import subprocess
import sys

INSTALL_DIR = os.path.expanduser("~/.ai-code-assistant")
BIN_PATH = "/usr/local/bin/ai-code"

def check_ollama():
    """Check if Ollama is installed, otherwise prompt to install."""
    if shutil.which("ollama") is None:
        print("⚠️ Ollama is not installed!")
        choice = input("Do you want to install Ollama? (y/n): ").strip().lower()
        if choice == "y":
            subprocess.run(["curl", "-fsSL", "https://ollama.ai/install.sh", "|", "bash"], check=True)
        else:
            print("❌ Ollama is required to run AI Code Assistant.")
            sys.exit(1)

def setup_files():
    """Download and move necessary files."""
    os.makedirs(INSTALL_DIR, exist_ok=True)
    
    # List of required files
    files = ["git_review.py", "codereview.py", "updater.py", "prompt.txt"]

    for file in files:
        url = f"https://raw.githubusercontent.com/jaencarlosap/ai-code-assistant/main/{file}"
        local_path = os.path.join(INSTALL_DIR, file)
        subprocess.run(["curl", "-fsSL", "-o", local_path, url], check=True)
        # Make main script executable
        subprocess.run(["chmod", "+x", local_path], check=True)
        

def main():
    print("📥 Installing AI Code Assistant...")
    check_ollama()
    setup_files()
    print("✅ Installation complete! Run 'ai-code --help' to get started.")

if __name__ == "__main__":
    main()
