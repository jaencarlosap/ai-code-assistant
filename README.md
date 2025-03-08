# AI Code Assistant

AI-powered Git code review using Ollama models.

## 🚀 Installation

Run the following commands to install the script globally:

```bash
chmod +x install.sh
./install.sh
```

This will install the assistant in `~/.ai-code-assistant` and create a global command `ai-code`.

## 📌 Usage

### Run AI Code Review

```bash
ai-code --review
```

### Update to the Latest Version

```bash
ai-code --update
```

### Show Help

```bash
ai-code --help
```

## 🔄 How It Works

- Fetches Git changes (both staged & unstaged).
- Sends them to an **Ollama AI model** for review.
- Streams the AI response live in the terminal.

## 🛠 Dependencies

Make sure you have **Python 3** and **Ollama** installed:

```bash
pip install ollama
```

## 🚀 Enjoy AI-powered code reviews from anywhere!
