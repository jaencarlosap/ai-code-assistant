import subprocess
import requests
import os
import sys

# Define the version of the script
VERSION = "1.0.0"

# URL to check the latest version (update with your repo)
VERSION_URL = "https://raw.githubusercontent.com/<your-username>/<your-repo>/main/VERSION"

# Get the directory of the script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def check_for_updates():
    """Check if there is a new version available."""
    try:
        response = requests.get(VERSION_URL, timeout=5)
        latest_version = response.text.strip()

        if latest_version != VERSION:
            print(f"\n🚀 A new version ({latest_version}) is available!")
            print("🔄 Updating automatically...\n")
            update_script()
        else:
            print("✅ You are using the latest version.")
    except Exception as e:
        print(f"⚠️ Could not check for updates: {e}")


def update_script():
    """Pull the latest version from GitHub and reinstall."""
    try:
        # Pull latest changes
        subprocess.run(["git", "-C", SCRIPT_DIR, "pull"], check=True)

        # Re-run the install command
        install_script = os.path.join(SCRIPT_DIR, "install.sh")
        if os.path.exists(install_script):
            subprocess.run(["bash", install_script], check=True)
            print("✅ Update completed! Please restart the script.")
            sys.exit(0)
        else:
            print("⚠️ Install script not found. Please run manually: git pull && ./install.sh")

    except subprocess.CalledProcessError as e:
        print(f"❌ Update failed: {e}")
        print("Please try updating manually: git pull && ./install.sh")
        sys.exit(1)


def main():
    # Check for manual update flag
    if len(sys.argv) > 1 and sys.argv[1] == "--update":
        print("🔄 Manually updating...")
        update_script()

    # Automatically check for updates on start
    check_for_updates()
    print("🚀 Running main script...")


if __name__ == "__main__":
    main()
