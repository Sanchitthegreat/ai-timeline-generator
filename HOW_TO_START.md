# 🚀 How to Start - Just Double-Click!

## 🎯 Super Easy - No Coding Required!

### For Windows Users 🪟

**Option 1: GUI Window (Recommended)**
- **Double-click** → `START_HERE_GUI.bat`
- Opens a nice window with buttons
- Click "Start Server"
- Browser opens automatically!

**Option 2: Console Window**
- **Double-click** → `START_HERE.bat`
- Opens terminal window
- Server starts automatically
- Browser opens automatically!

---

### For Mac Users 🍎

**Double-click** → `START_HERE.command`

**First time only:**
1. Right-click the file
2. Select "Open"
3. Click "Open" in the security dialog
4. (This allows it to run in the future)

**Browser opens automatically!**

---

### For Linux Users 🐧

**Double-click** → `START_HERE.sh`

**Or from terminal:**
```bash
chmod +x START_HERE.sh
./START_HERE.sh
```

**Browser opens automatically!**

---

## 🎬 What Happens When You Double-Click?

1. ✓ Checks Python is installed
2. ✓ Installs dependencies (first time only, ~1-2 minutes)
3. ✓ Starts web server
4. ✓ Opens browser automatically at `http://localhost:5000`
5. ✓ You're ready to use the app!

---

## ⚙️ First Time Setup (Automatic!)

When you run it for the first time:
- It will automatically install all required packages
- This takes 1-2 minutes
- You only need to do this once!

**Progress shown in the window:**
```
✓ Checking Python version...
✓ Checking dependencies...
  → Installing dependencies (first time only)...
  → This may take 1-2 minutes...
✓ Starting web server...
✓ Opening browser...
✅ SUCCESS!
```

---

## 🛑 How to Stop the Server?

- **Windows GUI**: Click the "Quit" button
- **Console/Terminal**: Close the window or press `Ctrl+C`

---

## 🐛 Troubleshooting

### "Python not found" error?

**Windows:**
1. Download Python from https://www.python.org/downloads/
2. **IMPORTANT**: Check "Add Python to PATH" during installation!
3. Restart your computer
4. Try again

**Mac:**
```bash
brew install python3
```
Or download from https://www.python.org/downloads/

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

---

### Mac security warning?

**"Cannot be opened because it is from an unidentified developer"**

**Solution:**
1. Right-click `START_HERE.command`
2. Select "Open"
3. Click "Open" in the dialog
4. Future runs will work with double-click

**Or via terminal:**
```bash
chmod +x START_HERE.command
xattr -d com.apple.quarantine START_HERE.command
./START_HERE.command
```

---

### Browser doesn't open automatically?

**Manual open:**
- Go to: `http://localhost:5000`

---

### Port already in use?

If you see "Port 5000 already in use":
1. Close any other running instance
2. Or open Task Manager/Activity Monitor
3. Kill any Python processes
4. Try again

---

## ✅ That's It!

**No coding, no terminal commands, just double-click!** 🎉

Once the browser opens:
1. Enter your OpenAI API key
2. Upload your SRT file
3. Generate timeline
4. Download XML for Premiere Pro

**See USAGE.md for detailed instructions on using the app.**

---

## 📝 Files Explained

| File | Purpose |
|------|---------|
| `START_HERE.bat` | Windows launcher (console) |
| `START_HERE_GUI.bat` | Windows launcher (GUI window) |
| `START_HERE.command` | Mac launcher |
| `START_HERE.sh` | Linux launcher |
| `launcher.py` | Main Python launcher script |
| `launcher_gui.pyw` | GUI launcher (Windows) |

**Just use the one for your operating system!**

---

**Happy Creating! 🎬✨**

