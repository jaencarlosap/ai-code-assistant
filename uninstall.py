import os
import shutil

INSTALL_DIR = os.path.expanduser("~/.ai-code-assistant")
BASHRC = os.path.expanduser("~/.bashrc")
ZSHRC = os.path.expanduser("~/.zshrc")
ALIAS_CMD = "alias ai-code='python3 ~/.ai-code-assistant/git_review.py'"

def remove_installation():
    """Removes the AI Code Assistant installation folder."""
    if os.path.exists(INSTALL_DIR):
        shutil.rmtree(INSTALL_DIR)
        print(f"✅ Removed {INSTALL_DIR}")
    else:
        print("⚠️ Installation folder not found.")

def remove_alias(file_path):
    """Removes the 'ai-code' alias from shell config files."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        with open(file_path, "w") as file:
            for line in lines:
                if "ai-code=" not in line:
                    file.write(line)

        print(f"✅ Removed alias from {file_path}")

def main():
    print("🚨 Uninstalling AI Code Assistant...")
    
    # Remove installation directory
    remove_installation()

    # Remove alias from shell config files
    remove_alias(BASHRC)
    remove_alias(ZSHRC)

    print("🎉 AI Code Assistant has been uninstalled!")
    print("⚠️ Restart your terminal or run 'source ~/.bashrc' (or 'source ~/.zshrc') for changes to take effect.")

if __name__ == "__main__":
    main()
