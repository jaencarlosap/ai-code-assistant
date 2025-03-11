import subprocess
import ollama
from shared.constants import MODEL_NAME, PROMPT_FILE_PATH

def start_ollama():
    """Start the Ollama service in the background."""
    try:
        subprocess.Popen(
            ['ollama', 'serve'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            start_new_session=True  
        )
        print("✅ Ollama service started in the background.")
    except Exception as e:
        print(f"❌ Error starting Ollama service: {e}")

def get_git_changes():
    """Get all unstaged and staged changes from git."""
    try:
        # Get unstaged and staged changes
        unstaged_changes = subprocess.run(["git", "diff", "HEAD"], capture_output=True, text=True).stdout
        staged_changes = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True).stdout
        
        changes = ""
        if unstaged_changes:
            changes += unstaged_changes
        if staged_changes:
            changes += staged_changes

        return changes.strip()
    except Exception as e:
        print(f"❌ Error running git diff: {e}")
        return ""

def analyze_code_with_ai(code_diff, model=MODEL_NAME):
    try:
        """Send code changes to an Ollama model for review and stream the response."""
        prompt_template = ""
        try:
            with open(PROMPT_FILE_PATH, "r") as file:
                prompt_template = file.read()
        except FileNotFoundError:
            print(f"❌ Error: prompt file not found at {PROMPT_FILE_PATH}.")
            return ""
        
        print("🤖 AI is thinking...\n")
        
        stream = ollama.chat(model=model, messages=[
            {"role": "user", "content": prompt_template},
            {"role": "user", "content": code_diff},
        ], stream=True)
        
        print("💡 Suggestions:\n")
        for chunk in stream:
            if "message" in chunk and "content" in chunk["message"]:
                print(chunk["message"]["content"], end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"❌ Error analyzing code with AI: {e}")
  

def main():
    try:
        start_ollama()
        git_changes = get_git_changes()
        
        if not git_changes:
            print("✅ No changes detected.")
            return
        
        print("\n🔍 Analyzing code changes...\n")
        analyze_code_with_ai(git_changes)
    except KeyboardInterrupt:
        print("\n🛑 AI processing interrupted.")
        return
    except Exception as e:
        print(f"❌ Error analyzing code with AI: {e}")
        return

if __name__ == "__main__":
    main()
