#!/usr/bin/env python3
"""
AI Timeline Generator - GUI Launcher (Windows - No Console)
This version runs without showing a console window
"""

import sys
import os
import subprocess
import time
import webbrowser
import threading
from pathlib import Path

# For Windows GUI
try:
    import tkinter as tk
    from tkinter import messagebox, scrolledtext
    HAS_TKINTER = True
except ImportError:
    HAS_TKINTER = False

class LauncherGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Timeline Generator")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Set icon if available
        try:
            # You can add an icon file later
            # self.root.iconbitmap('icon.ico')
            pass
        except:
            pass
        
        # Header
        header_frame = tk.Frame(self.root, bg="#667eea", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="🎬 AI Timeline Generator",
            font=("Arial", 20, "bold"),
            bg="#667eea",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Status text area
        self.status_text = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            width=70,
            height=15,
            font=("Courier", 10),
            bg="#f8f9fa",
            fg="#333"
        )
        self.status_text.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.start_button = tk.Button(
            button_frame,
            text="▶ Start Server",
            command=self.start_app,
            font=("Arial", 12, "bold"),
            bg="#28a745",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.quit_button = tk.Button(
            button_frame,
            text="✕ Quit",
            command=self.quit_app,
            font=("Arial", 12),
            bg="#dc3545",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.quit_button.pack(side=tk.LEFT, padx=5)
        
        self.log("Ready to start! Click 'Start Server' button.\n")
        
    def log(self, message):
        """Add message to status text"""
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.root.update()
        
    def start_app(self):
        """Start the application"""
        self.start_button.config(state=tk.DISABLED)
        self.log("="*60)
        self.log("Starting AI Timeline Generator...")
        self.log("="*60)
        
        # Run startup in thread
        thread = threading.Thread(target=self.run_startup, daemon=True)
        thread.start()
        
    def run_startup(self):
        """Run startup sequence"""
        try:
            # Check Python version
            self.log("\n✓ Checking Python version...")
            if sys.version_info < (3, 8):
                self.log(f"❌ ERROR: Python 3.8+ required!")
                self.log(f"   Your version: {sys.version}")
                messagebox.showerror("Error", "Python 3.8 or higher is required!")
                return
            self.log(f"  → Python {sys.version_info.major}.{sys.version_info.minor} ✓")
            
            # Install dependencies
            self.log("\n✓ Checking dependencies...")
            self.install_dependencies()
            
            # Start Flask
            self.log("\n✓ Starting web server...")
            self.log("  → Server: http://localhost:5000")
            self.log("\n" + "="*60)
            self.log("✅ SUCCESS! Opening browser...")
            self.log("="*60)
            self.log("\nTo stop: Close this window or click Quit button")
            
            # Open browser
            time.sleep(2)
            webbrowser.open("http://localhost:5000")
            
            # Start Flask in main thread
            self.root.after(100, self.start_flask)
            
        except Exception as e:
            self.log(f"\n❌ ERROR: {e}")
            messagebox.showerror("Error", str(e))
            self.start_button.config(state=tk.NORMAL)
    
    def install_dependencies(self):
        """Install required packages"""
        try:
            import flask
            import openai
            import pysrt
            self.log("  → All dependencies installed ✓")
        except ImportError:
            self.log("  → Installing dependencies (first time)...")
            self.log("  → This may take 1-2 minutes...")
            
            script_dir = Path(__file__).parent
            requirements = script_dir / "requirements.txt"
            
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "-q", "-r", str(requirements)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            self.log("  → Dependencies installed ✓")
    
    def start_flask(self):
        """Start Flask app"""
        try:
            script_dir = Path(__file__).parent
            os.chdir(script_dir)
            sys.path.insert(0, str(script_dir))
            
            from app import app
            app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
        except Exception as e:
            self.log(f"\n❌ Flask error: {e}")
            messagebox.showerror("Server Error", str(e))
    
    def quit_app(self):
        """Quit the application"""
        if messagebox.askokcancel("Quit", "Stop the server and close?"):
            self.root.quit()
            sys.exit(0)
    
    def run(self):
        """Run the GUI"""
        self.root.protocol("WM_DELETE_WINDOW", self.quit_app)
        self.root.mainloop()

def main():
    """Main function"""
    if HAS_TKINTER:
        app = LauncherGUI()
        app.run()
    else:
        # Fallback to console version
        print("Tkinter not available, using console version...")
        import launcher
        launcher.main()

if __name__ == "__main__":
    main()

