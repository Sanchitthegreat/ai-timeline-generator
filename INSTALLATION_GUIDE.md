# 📦 Installation Guide - Visual Step-by-Step

## 🎯 Goal: Get the App Running in 2 Minutes

No coding knowledge required! Just follow these simple steps.

---

## Step 1: Download the Project ⬇️

You should have a folder called `ai-timeline-generator` with these files:

```
ai-timeline-generator/
│
├── 🚀 START HERE 🚀.txt       ← READ THIS FIRST!
│
├── 📁 For Windows:
│   ├── START_HERE_GUI.bat      ← DOUBLE-CLICK THIS! (Recommended)
│   └── START_HERE.bat          ← Or this (console version)
│
├── 📁 For Mac:
│   └── START_HERE.command      ← DOUBLE-CLICK THIS!
│
├── 📁 For Linux:
│   └── START_HERE.sh           ← DOUBLE-CLICK THIS!
│
└── 📁 Documentation:
    ├── HOW_TO_START.md         ← Troubleshooting
    ├── QUICKSTART.md           ← Quick guide
    ├── USAGE.md                ← How to use
    └── README.md               ← Full docs
```

---

## Step 2: Make Sure Python is Installed 🐍

### Check if you have Python:

**Windows:**
- Press `Win + R`
- Type `cmd` and press Enter
- Type `python --version`
- Should show "Python 3.8" or higher

**Mac/Linux:**
- Open Terminal
- Type `python3 --version`
- Should show "Python 3.8" or higher

### Don't have Python? Install it:

**Windows:**
1. Go to https://www.python.org/downloads/
2. Download the latest Python 3
3. Run the installer
4. ⚠️ **IMPORTANT**: Check "Add Python to PATH"
5. Click "Install Now"

**Mac:**
```bash
# Using Homebrew
brew install python3
```
Or download from https://www.python.org/downloads/

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
```

---

## Step 3: Run the Launcher! 🚀

### 🪟 **Windows Users:**

#### Option A: GUI Window (Easiest!)

1. Find `START_HERE_GUI.bat` in the folder
2. **Double-click it**
3. A window opens with buttons
4. Click "Start Server"
5. Browser opens automatically!

#### Option B: Console Window

1. Find `START_HERE.bat` in the folder
2. **Double-click it**
3. Console window opens
4. Wait for "SUCCESS!" message
5. Browser opens automatically!

**Screenshot of what you'll see:**
```
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║        🎬 AI TIMELINE GENERATOR 🎬                   ║
║                                                       ║
║        Starting up... Please wait...                  ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝

✓ Checking Python version...
  → Python 3.11 detected ✓

✓ Checking dependencies...
  → Installing dependencies (first time only)...
  → This may take 1-2 minutes...
  → Dependencies installed successfully ✓

✓ Starting web server...
  → Server starting on http://localhost:5000

============================================================
✅ SUCCESS! The app is now running!
============================================================

📌 Your browser should open automatically...
   If not, open: http://localhost:5000
```

---

### 🍎 **Mac Users:**

1. Find `START_HERE.command` in the folder
2. **Right-click** it (first time only)
3. Select **"Open"**
4. Click **"Open"** in the security dialog
5. Terminal opens
6. Wait for "SUCCESS!" message
7. Browser opens automatically!

**Next time:** Just double-click it!

**Alternative (if double-click doesn't work):**
```bash
cd /path/to/ai-timeline-generator
chmod +x START_HERE.command
./START_HERE.command
```

---

### 🐧 **Linux Users:**

1. Find `START_HERE.sh` in the folder
2. **Double-click it**
3. Select "Run in Terminal" if prompted
4. Wait for "SUCCESS!" message
5. Browser opens automatically!

**Alternative:**
```bash
cd /path/to/ai-timeline-generator
chmod +x START_HERE.sh
./START_HERE.sh
```

---

## Step 4: First Time Setup (Automatic!) ⚙️

**First time you run it:**
- The launcher will automatically install all required packages
- This takes **1-2 minutes**
- You'll see progress messages
- This only happens once!

**What gets installed:**
- Flask (web framework)
- OpenAI (for GPT-4o)
- Pillow (image processing)
- pysrt (SRT parsing)
- requests (API calls)

**Total download size:** ~50MB

---

## Step 5: Browser Opens! 🌐

After setup completes, your default browser will automatically open to:

```
http://localhost:5000
```

You'll see a beautiful purple gradient page with:
- **Title:** "AI Timeline Generator"
- **API Key input field**
- **File upload button**
- **Generate button**

---

## Step 6: Get Your OpenAI API Key 🔑

1. Go to https://platform.openai.com/api-keys
2. Sign in (or create account)
3. Click **"Create new secret key"**
4. Copy the key (starts with `sk-`)
5. ⚠️ **IMPORTANT:** Add billing/credits to your OpenAI account

**Cost:** ~$0.20 per 100 images (super cheap!)

---

## Step 7: Generate Your First Timeline! 🎬

1. Paste your OpenAI API key in the input field
2. Click "Choose SRT File"
3. Upload `example_script.srt` (included in the folder)
4. Click **"Generate Timeline"**
5. Wait 5-10 minutes (for the example, which generates ~8 images)
6. Download the XML file
7. Import into Premiere Pro!

---

## 🎉 You're Done!

The app is now running. You can:
- ✅ Upload your own SRT files
- ✅ Generate as many timelines as you want
- ✅ Leave it running in the background

---

## 🛑 How to Stop the App

**Windows GUI:**
- Click the "Quit" button in the window

**Console/Terminal:**
- Close the window
- Or press `Ctrl + C`

---

## 🐛 Troubleshooting

### "Python not found" error

**Solution:** Install Python (see Step 2 above)

**Windows specific:** Make sure "Add Python to PATH" was checked during installation

---

### Mac security warning

**Error:** "Cannot be opened because it is from an unidentified developer"

**Solution:**
1. Right-click `START_HERE.command`
2. Select "Open"
3. Click "Open" in the dialog

Or via terminal:
```bash
xattr -d com.apple.quarantine START_HERE.command
```

---

### Dependencies fail to install

**Error:** "Failed to install dependencies"

**Solution:**
```bash
# Try manual installation
cd ai-timeline-generator
pip install -r requirements.txt
```

If that fails:
```bash
# Upgrade pip first
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### Port 5000 already in use

**Error:** "Address already in use"

**Solution:**
1. Close any other running instance of the app
2. Check Task Manager (Windows) or Activity Monitor (Mac)
3. Kill any Python processes
4. Try again

Or edit `app.py` line at the end:
```python
app.run(host='0.0.0.0', port=5560)  # Change to 5560
```

---

### Browser doesn't open automatically

**Solution:**
- Manually open your browser
- Go to: `http://localhost:5000`

---

## 📚 Next Steps

Once the app is running:
- Read **USAGE.md** for detailed usage instructions
- Try the included `example_script.srt`
- Create your own SRT files
- Generate amazing timelines!

---

## 💡 Pro Tips

1. **Keep the console/terminal window open** while using the app
2. **Bookmark** `http://localhost:5000` for quick access
3. **Create a desktop shortcut** to the launcher file
4. **First test** with the example file before using your own
5. **Read the theme** that GPT-4o detects to ensure it matches your vision

---

## 🎓 Learning More

- **QUICKSTART.md** → 3-minute quick start
- **USAGE.md** → Complete usage guide
- **README.md** → Full documentation
- **PROJECT_OVERVIEW.md** → Technical details

---

## ✅ Summary Checklist

- [ ] Python 3.8+ installed
- [ ] Downloaded ai-timeline-generator folder
- [ ] Double-clicked the launcher file
- [ ] Dependencies auto-installed
- [ ] Browser opened automatically
- [ ] Got OpenAI API key
- [ ] Uploaded example SRT
- [ ] Generated first timeline
- [ ] Imported to Premiere Pro

**Congratulations! You're all set! 🎉**

---

**Need help? Check HOW_TO_START.md or USAGE.md**

**Happy Creating! 🚀✨**

