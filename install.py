import os
import shutil
import subprocess
import sys

INSTALL_DIR = os.path.expanduser("~/.ai-code-assistant")
REPO_URL = "https://github.com/jaencarlosap/ai-code-assistant.git"
MODEL_NAME = "qwen2.5-coder:7b"

def check_ollama():
    """Check if Ollama is installed, otherwise prompt to install."""
    IS_LINUX = sys.platform.startswith("linux")
    IS_MAC = sys.platform == "darwin"
    IS_WINDOWS = sys.platform == "win32"

    if shutil.which("ollama") is None:
        print("⚠️ Ollama is not installed!")
        choice = input("Do you want to install Ollama? (y/n): ").strip().lower()
        if choice == "y":
            if IS_LINUX:
                subprocess.run('curl -fsSL https://ollama.com/install.sh | sh', check=True)
            elif IS_MAC:
                subprocess.run(['brew', 'install', 'ollama'], check=True)
            elif IS_WINDOWS:
                print("📦 Download from: https://ollama.com")
        else:
            print("❌ Ollama is required to run AI Code Assistant.")
            print("📦 Download from: https://ollama.com")
            sys.exit(1)

def check_ollama_model():
    """Check if the required Ollama model is installed."""
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
        installed_models = result.stdout

        if MODEL_NAME in installed_models:
            return True  # Model is installed
        else:
            print(f"❌ Model '{MODEL_NAME}' not found. Please install it using:\n")
            # ask to install
            choice = input("Do you want to install the model? (y/n): ").strip().lower()
            if choice == "y":
                subprocess.run(["ollama", "install", MODEL_NAME], check=True)
                return True
            else:
                print("❌ Model is required to run AI Code Assistant.")
                sys.exit()
                return False

    except subprocess.CalledProcessError as e:
        print(f"❌ Error checking for Ollama model: {e}")
        return False

def clone_repository():
    """Clone or update the repository."""
    if os.path.exists(INSTALL_DIR) and os.path.exists(os.path.join(INSTALL_DIR, ".git")):
        print("🔄 Updating AI Code Assistant...")
        subprocess.run(["git", "-C", INSTALL_DIR, "pull"], check=True)
    else:
        print("📥 Cloning AI Code Assistant repository...")
        subprocess.run(["git", "clone", REPO_URL, INSTALL_DIR], check=True)

def install_requirements():
    """Install the required Python packages."""
    subprocess.run(["pip3", "install", "-r", f"{INSTALL_DIR}/requirements.txt"], check=True)

def adding_alias():
    """Add the 'ai-code' alias to the shell config file."""
    try:
        alias_cmd = f"alias ai-code='python3 {INSTALL_DIR}/main.py'"
        shell_config_files = [os.path.expanduser("~/.zshrc"), os.path.expanduser("~/.bashrc")]

        for file_path in shell_config_files:
            if os.path.exists(file_path):
                subprocess.run(["sudo", "bash", "-c", f"echo '\n# AI Code Assistant\n{alias_cmd}' >> {file_path}"], check=True)
                print(f"✅ Alias added to {file_path}")

        print("🚀 Restart your terminal or run `exec $SHELL` to apply changes.")

    except Exception as e:
        print(f"❌ Error adding alias: {e}")
    

def main():
    try:
        print("🚀 Installing AI Code Assistant...")
        check_ollama()
        check_ollama_model()
        clone_repository()
        install_requirements()
        adding_alias()
        print("✅ Installation complete! Run 'ai-code --help' to get started.")
    except Exception:
        print("❌ Operation cancelled.")

if __name__ == "__main__":
    main()
