import subprocess
import ollama
import os

# Global model name
MODEL_NAME = "qwen2.5-coder:7b"

# Determine the directory of the current script and set the prompt file path dynamically
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_FILE_PATH = os.path.join(SCRIPT_DIR, "prompt.txt")

def get_git_changes():
    """Get all unstaged and staged changes from git."""
    try:
        # Get unstaged and staged changes
        unstaged_changes = subprocess.run(["git", "diff", "HEAD"], capture_output=True, text=True).stdout
        staged_changes = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True).stdout
        
        changes = ""
        if unstaged_changes:
            changes += "\n### Unstaged Changes ###\n" + unstaged_changes
        if staged_changes:
            changes += "\n### Staged Changes ###\n" + staged_changes

        return changes.strip()
    except Exception as e:
        print(f"❌ Error running git diff: {e}")
        return ""

def analyze_code_with_ai(code_diff, model=MODEL_NAME):
    """Send code changes to an Ollama model for review."""
    try:
        with open(PROMPT_FILE_PATH, "r") as file:
            prompt_template = file.read()
    except FileNotFoundError:
        print(f"❌ Error: prompt file not found at {PROMPT_FILE_PATH}.")
        return ""
    
    prompt = prompt_template.format(code_diff=code_diff)
    
    print("🤖 AI is thinking...\n")
    
    stream = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}], stream=True)
    
    print("💡 Suggestions:\n")
    for chunk in stream:
        if "message" in chunk and "content" in chunk["message"]:
            print(chunk["message"]["content"], end="", flush=True)
    print("\n")

def main():
    git_changes = get_git_changes()
    
    if not git_changes:
        print("✅ No changes detected.")
        return
    
    print("\n🔍 Analyzing code changes...\n")
    analyze_code_with_ai(git_changes)

if __name__ == "__main__":
    main()
