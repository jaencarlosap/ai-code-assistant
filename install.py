import os
import shutil
import subprocess

INSTALL_DIR = os.path.expanduser("~/.ai-code-assistant")
BASHRC = os.path.expanduser("~/.bashrc")
ZSHRC = os.path.expanduser("~/.zshrc")
ALIAS_CMD = "alias ai-code='python3 ~/.ai-code-assistant/git_review.py'"

def check_ollama():
    """Check if Ollama is installed and prompt to install if missing."""
    try:
        subprocess.run(["ollama", "--version"], check=True, stdout=subprocess.DEVNULL)
        print("✅ Ollama is already installed.")
    except FileNotFoundError:
        print("⚠️ Ollama is not installed.")
        install = input("Do you want to install Ollama now? (y/n): ").strip().lower()
        if install == "y":
            subprocess.run(["curl", "-fsSL", "https://ollama.com/install.sh", "|", "sh"], shell=True)
        else:
            print("⚠️ Skipping Ollama installation.")

def create_install_dir():
    """Creates the installation directory."""
    if not os.path.exists(INSTALL_DIR):
        os.makedirs(INSTALL_DIR)
        print(f"✅ Created installation directory at {INSTALL_DIR}")
    else:
        print("✅ Installation directory already exists.")

def copy_files():
    """Copies necessary files to the installation directory."""
    files_to_copy = ["git_review.py", "codereview.py", "updater.py", "prompt.txt"]
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy(file, INSTALL_DIR)
            print(f"✅ Copied {file} to {INSTALL_DIR}")
        else:
            print(f"⚠️ Warning: {file} not found.")

def add_alias(file_path):
    """Adds alias to the shell configuration file."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            if ALIAS_CMD in file.read():
                return  # Alias already exists
    
    with open(file_path, "a") as file:
        file.write(f"\n{ALIAS_CMD}\n")
    print(f"✅ Alias added to {file_path}")

def main():
    print("🚀 Installing AI Code Assistant...")

    check_ollama()
    create_install_dir()
    copy_files()
    
    add_alias(BASHRC)
    add_alias(ZSHRC)

    print("🎉 Installation complete! Restart your terminal or run 'source ~/.bashrc' (or 'source ~/.zshrc').")

if __name__ == "__main__":
    main()
