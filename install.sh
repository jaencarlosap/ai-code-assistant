#!/bin/bash

# Ensure script is run from its directory
cd "$(dirname "$0")"

echo "🚀 Installing git-review-ai..."

# Install the package
pip install --user .

# Ensure the binary path is in the user's PATH
USER_BIN="$HOME/.local/bin"
if [[ ":$PATH:" != *":$USER_BIN:"* ]]; then
    echo "export PATH=\"$USER_BIN:\$PATH\"" >> ~/.bashrc
    echo "export PATH=\"$USER_BIN:\$PATH\"" >> ~/.zshrc
    source ~/.bashrc || source ~/.zshrc
fi

echo "✅ Installation complete!"
echo "You can now run 'git-review-ai' from anywhere."
