#!/usr/bin/env python3
"""
AI Timeline Generator - Auto Launcher
Double-click this file to start the app!
"""

import sys
import os
import subprocess
import time
import webbrowser
import threading
from pathlib import Path

def print_banner():
    """Print startup banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║        🎬 AI TIMELINE GENERATOR 🎬                   ║
    ║                                                       ║
    ║        Starting up... Please wait...                  ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version is sufficient"""
    print("✓ Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ ERROR: Python 3.8 or higher required!")
        print(f"   Your version: {sys.version}")
        input("\nPress Enter to exit...")
        sys.exit(1)
    print(f"  → Python {sys.version_info.major}.{sys.version_info.minor} detected ✓")

def setup_venv():
    """Setup virtual environment"""
    script_dir = Path(__file__).parent
    venv_dir = script_dir / "venv"
    
    # Check if venv exists
    if venv_dir.exists() and (venv_dir / "bin" / "python3").exists():
        venv_python = venv_dir / "bin" / "python3"
        return venv_python
    
    # Create venv if it doesn't exist
    print("  → Creating virtual environment...")
    try:
        subprocess.check_call([
            sys.executable,
            "-m",
            "venv",
            str(venv_dir)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        venv_python = venv_dir / "bin" / "python3"
        print("  → Virtual environment created ✓")
        return venv_python
    except subprocess.CalledProcessError as e:
        print(f"❌ ERROR: Failed to create virtual environment!")
        print(f"   Error: {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)

def install_dependencies():
    """Install required packages"""
    print("\n✓ Checking dependencies...")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print("❌ ERROR: requirements.txt not found!")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    # Setup virtual environment
    venv_python = setup_venv()
    
    # Check if packages are installed in venv
    try:
        result = subprocess.run([
            str(venv_python),
            "-c",
            "import flask, openai, pysrt, replicate"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            # Check optional dependencies (diffusers, torch) - warn if missing but don't fail
            optional_check = subprocess.run([
                str(venv_python),
                "-c",
                "import diffusers, torch"
            ], capture_output=True, text=True)
            
            if optional_check.returncode == 0:
                print("  → All dependencies already installed ✓")
            else:
                print("  → Core dependencies installed ✓")
                print("  → Note: Local Drawatoon model requires diffusers & torch")
            return venv_python
    except Exception:
        pass
    
    # Install dependencies in venv
    print("  → Installing dependencies (first time only)...")
    print("  → This may take 3-5 minutes (including torch & diffusers)...")
    
    try:
        subprocess.check_call([
            str(venv_python),
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip",
            "-q"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        print("  → Installing core packages...")
        subprocess.check_call([
            str(venv_python),
            "-m",
            "pip",
            "install",
            "-q",
            "-r",
            str(requirements_file)
        ])
        print("  → Dependencies installed successfully ✓")
        return venv_python
    except subprocess.CalledProcessError as e:
        print(f"❌ ERROR: Failed to install dependencies!")
        print(f"   Error: {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)

def open_browser(port=5560, delay=3):
    """Open browser after delay"""
    time.sleep(delay)
    url = f"http://localhost:{port}"
    print(f"\n✓ Opening browser at {url}...")
    webbrowser.open(url)

def start_flask_app(venv_python):
    """Start the Flask application"""
    print("\n✓ Starting web server...")
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Check if app.py exists
    if not (script_dir / "app.py").exists():
        print("❌ ERROR: app.py not found!")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    # Start browser opener in background
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    print("  → Server starting on http://localhost:5560")
    print("\n" + "="*60)
    print("✅ SUCCESS! The app is now running!")
    print("="*60)
    print("\n📌 Your browser should open automatically...")
    print("   If not, open: http://localhost:5560")
    print("\n📌 To stop the server:")
    print("   → Close this window")
    print("   → Or press Ctrl+C")
    print("\n" + "="*60 + "\n")
    
    # Start Flask app using venv Python
    try:
        subprocess.run([str(venv_python), str(script_dir / "app.py")])
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped by user")
    except Exception as e:
        print(f"\n❌ ERROR: Failed to start server!")
        print(f"   Error: {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)

def main():
    """Main launcher function"""
    try:
        print_banner()
        check_python_version()
        venv_python = install_dependencies()
        start_flask_app(venv_python)
    except KeyboardInterrupt:
        print("\n\n✓ Startup cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()

