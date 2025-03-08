#!/bin/bash

INSTALL_DIR="$HOME/.ai-code-assistant"
BIN_DIR="$HOME/.local/bin"
EXECUTABLE_NAME="ai-code"

# Create necessary directories
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

# Copy all files to the installation directory
cp -r ./* "$INSTALL_DIR"

# Create a wrapper script for global execution
echo "#!/bin/bash
python3 $INSTALL_DIR/git_review.py \"\$@\"" > "$BIN_DIR/$EXECUTABLE_NAME"

# Give execution permissions
chmod +x "$BIN_DIR/$EXECUTABLE_NAME"

# Add the bin directory to PATH if not already present
if ! grep -qxF "export PATH=\$HOME/.local/bin:\$PATH" "$HOME/.bashrc"; then
    echo "export PATH=\$HOME/.local/bin:\$PATH" >> "$HOME/.bashrc"
fi
if ! grep -qxF "export PATH=\$HOME/.local/bin:\$PATH" "$HOME/.zshrc"; then
    echo "export PATH=\$HOME/.local/bin:\$PATH" >> "$HOME/.zshrc"
fi

# Reload shell configuration
source "$HOME/.bashrc" 2>/dev/null || source "$HOME/.zshrc" 2>/dev/null

echo "✅ Installation complete! You can now use 'ai-code' from anywhere."