#!/bin/bash
# AI Timeline Generator - Linux Launcher
# Double-click this file to start the app!

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "========================================"
    echo "   ERROR: Python 3 not found!"
    echo "========================================"
    echo ""
    echo "Please install Python 3.8 or higher:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  Fedora: sudo dnf install python3 python3-pip"
    echo "  Arch: sudo pacman -S python python-pip"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# Make launcher executable
chmod +x launcher.py

# Run the launcher
python3 launcher.py

# Keep terminal open
echo ""
read -p "Press Enter to close..."

