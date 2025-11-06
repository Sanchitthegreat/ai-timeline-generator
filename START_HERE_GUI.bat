@echo off
REM AI Timeline Generator - Windows GUI Launcher
REM Double-click this file for a nice GUI window!

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    msg * "Python not found! Please install Python 3.8 or higher from https://www.python.org/downloads/"
    exit /b 1
)

REM Run the GUI launcher (no console window)
start "" pythonw "%~dp0launcher_gui.pyw"

