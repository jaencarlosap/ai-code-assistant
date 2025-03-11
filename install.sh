#!/bin/bash

# Exit on error
set -e

echo "🚀 Installing AI Code Assistant..."

# Define install directory
INSTALL_DIR="$HOME/.ai-code-assistant"

# Create install directory
mkdir -p "$INSTALL_DIR"

# Download install.py
echo "⬇️ Downloading installation script..."
curl -fsSL -o "$INSTALL_DIR/install.py" "https://raw.githubusercontent.com/jaencarlosap/ai-code-assistant/main/install.py"

# Run Python install script
echo "⚙️ Running installation..."
python3 "$INSTALL_DIR/install.py"

echo "✅ Installation completed!"
echo "➡️ Run 'ai-code --help' to get started."
