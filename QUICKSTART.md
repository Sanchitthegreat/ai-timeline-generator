# ⚡ Quick Start Guide - 3 Minutes to First Timeline

## 1️⃣ Start the App (Just Double-Click!)

### 🪟 **Windows:**
- Double-click → `START_HERE_GUI.bat` (recommended)
- OR → `START_HERE.bat`

### 🍎 **Mac:**
- Double-click → `START_HERE.command`

### 🐧 **Linux:**
- Double-click → `START_HERE.sh`

**Browser opens automatically at http://localhost:5000**

---

### 🔧 **OR Manual Method:**

```bash
cd ai-timeline-generator
pip install -r requirements.txt
python app.py
```

Open: **http://localhost:5000**

## 3️⃣ Get API Key (2 minutes)

1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-`)
4. ⚠️ **IMPORTANT**: Add billing to your OpenAI account

## 4️⃣ Generate (5-10 minutes)

1. Paste your API key in the web app
2. Upload your SRT file (or use `example_script.srt`)
3. Click "Generate Timeline"
4. Wait for processing
5. Download the XML file

## 5️⃣ Import to Premiere Pro (1 minute)

1. Open Premiere Pro
2. File → Import → Select XML
3. Done! 🎉

---

## 📄 Need an SRT file?

Use `example_script.srt` included in the project!

Or create one:

```srt
1
00:00:01,000 --> 00:00:04,500
Your first line of dialogue or description

2
00:00:04,500 --> 00:00:08,200
Your second line continues the story

3
00:00:08,200 --> 00:00:12,000
And so on...
```

---

## 💰 Cost?

**~$0.20 per 100 images** (only GPT-4o calls)

HuggingFace image generation is **completely FREE!**

---

## 🐛 Issues?

**"Model loading" error?**
→ Wait 30 seconds, HuggingFace free tier has cold starts

**"Invalid API key"?**
→ Make sure billing is enabled on OpenAI account

**Slow processing?**
→ Normal! ~1-2 minutes per image on free tier

---

## 📚 Want More Details?

- **README.md** → Full installation guide
- **USAGE.md** → Detailed usage & configuration
- **PROJECT_OVERVIEW.md** → Technical deep dive

---

**That's it! Start creating! 🚀**

