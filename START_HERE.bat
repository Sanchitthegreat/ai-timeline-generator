@echo off
REM AI Timeline Generator - Windows Launcher
REM Double-click this file to start the app!

title AI Timeline Generator

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ========================================
    echo    ERROR: Python not found!
    echo ========================================
    echo.
    echo Please install Python 3.8 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

REM Run the launcher
python "%~dp0launcher.py"

REM Keep window open if there was an error
if %errorlevel% neq 0 (
    echo.
    echo Press any key to exit...
    pause >nul
)

