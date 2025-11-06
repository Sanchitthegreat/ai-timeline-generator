#!/bin/bash
# AI Timeline Generator - Mac Launcher
# Double-click this file to start the app!

# Get the directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# Open Terminal window if not already in terminal
if [ -z "$TERM" ]; then
    osascript -e 'tell application "Terminal" to do script "cd \"'"$DIR"'\" && python3 launcher.py"' > /dev/null 2>&1
    exit 0
fi

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    osascript -e 'display dialog "Python 3 is not installed!\n\nPlease install Python 3.8 or higher from:\nhttps://www.python.org/downloads/" buttons {"OK"} default button "OK" with icon stop'
    exit 1
fi

# Run the launcher
python3 launcher.py

# Keep terminal open if user wants to see output
echo ""
echo "Press any key to close..."
read -n 1 -s
