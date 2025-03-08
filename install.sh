#!/bin/bash

# Ensure script runs from its directory
cd "$(dirname "$0")"

# Function to get the latest version from GitHub
get_latest_version() {
    curl -s https://raw.githubusercontent.com/jaencarlosap/ai-code-assistant/main/VERSION
}

# Get the installed version
INSTALLED_VERSION=$(cat VERSION)
LATEST_VERSION=$(get_latest_version)

# Check if an update is needed
if [[ "$INSTALLED_VERSION" != "$LATEST_VERSION" ]]; then
    echo "🚀 A new version ($LATEST_VERSION) is available!"
    echo "Run the following command to update:"
    echo "  git pull && ./install.sh"
    exit 0
fi

echo "✅ You have the latest version: $INSTALLED_VERSION"

# Install the package
pip install --user .

# Ensure the binary path is in the user's PATH
USER_BIN="$HOME/.local/bin"
if [[ ":$PATH:" != *":$USER_BIN:"* ]]; then
    echo "export PATH=\"$USER_BIN:\$PATH\"" >> ~/.bashrc
    echo "export PATH=\"$USER_BIN:\$PATH\"" >> ~/.zshrc
    source ~/.bashrc || source ~/.zshrc
fi

echo "✅ Installation complete! You can now run 'git-review-ai'."
