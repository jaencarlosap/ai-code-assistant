# Ai code assistant

This script reviews Git changes using an AI model from Ollama. It checks for best practices and potential issues in code changes before committing them.

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Git
- Ollama CLI ([Install Ollama](https://ollama.com))

## Installation

1. **Clone the repository** (or copy the script to your desired location):

   ```sh
   git clone https://github.com/jaencarlosap/ai-code-assistant
   cd ai-code-assitant
   ```

2. **Install dependencies:**

   ```sh
   pip install ollama
   ```

3. **Download the AI model:**

   ```sh
   ollama pull qwen2.5-coder:7b
   ```

4. **Ensure you have a `prompt.txt` file in the same directory as the script.** Example:

   ```txt
   ### Code Review Task
   Review the following code changes and ensure they follow best practices.

   {code_diff}

   ### Review Feedback:
   ```

## Usage

Run the script inside a Git repository:

```sh
python script.py
```

## How It Works

- Fetches all unstaged and staged changes using `git diff`.
- Loads a predefined prompt from `prompt.txt`.
- Sends the changes to the AI model for review.
- Streams the AI-generated suggestions to the console.

## Troubleshooting

- If the script fails to find `prompt.txt`, ensure it's in the same directory.
- If `ollama` command is not found, verify Ollama is installed and added to `PATH`.
- If no changes are detected, check if your Git working directory has modifications.

## License

MIT License.
