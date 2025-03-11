import os

# Global model name
MODEL_NAME = "qwen2.5-coder:7b"

# Determine the directory of the current script and set the prompt file path dynamically
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_FILE_PATH = os.path.join(SCRIPT_DIR, "prompt.txt")

INSTALL_DIR = os.path.expanduser("~/.ai-code-assistant")
REPO_URL = "https://github.com/jaencarlosap/ai-code-assistant.git"
MODEL_NAME = "qwen2.5-coder:7b"

BASHRC = os.path.expanduser("~/.bashrc")
ZSHRC = os.path.expanduser("~/.zshrc")
ALIAS_CMD = "alias ai-code='python3 {INSTALL_DIR}/main.py'"
