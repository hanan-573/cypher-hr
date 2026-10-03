# start.py
# Usage: python start.py

import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS = os.path.join(BASE_DIR, "requirements.txt")
MAIN_FILE = os.path.join(BASE_DIR, "firewall.py")


def requirements_installed():
    """Check if the required packages are already installed."""
    try:
        import reportlab
        import colorama
        import pick
        return True
    except ImportError:
        return False


def install_requirements():
    print("Installing requirements, please wait...")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS]
    )
    print("Requirements installed.\n")


def main():
    if not requirements_installed():
        install_requirements()
    else:
        print("Requirements already installed.\n")

    print("Starting project...\n")
    subprocess.run([sys.executable, MAIN_FILE], cwd=BASE_DIR)


if __name__ == "__main__":
    main()
