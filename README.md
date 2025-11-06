# 🎬 AI Timeline Generator

**Automatically generate visual timelines from script + SRT files using AI**

Convert your video scripts (SRT format) into AI-generated images synced to timestamps, ready to import into Premiere Pro.

## 🚀 Features

- **Automatic Scene Detection**: Intelligently groups 1-4 subtitle lines into logical visual segments
- **AI Theme Analysis**: Uses GPT-4o to detect overall visual style from your script
- **Smart Prompt Generation**: GPT-4o creates optimized SDXL prompts for each scene
- **Free Image Generation**: Uses HuggingFace Inference API (Stable Diffusion XL)
- **Timeline Sync**: Maps images to exact SRT timestamps
- **Premiere Pro Export**: Generates XML files ready to import into Adobe Premiere Pro

## 💰 Cost

**~$0.20-0.30 per 100 images** (only GPT-4o API calls, HuggingFace is free!)

## 📋 Requirements

- Python 3.8+
- OpenAI API key (for GPT-4o)
- Internet connection (for HuggingFace API)

## 🛠️ Installation

### 🚀 **EASY METHOD - Just Double-Click! (No Terminal Required)**

**Windows:**
- Double-click → `START_HERE_GUI.bat` (GUI window) 
- OR → `START_HERE.bat` (console)

**Mac:**
- Double-click → `START_HERE.command`
- (First time: Right-click → Open)

**Linux:**
- Double-click → `START_HERE.sh`

**That's it!** The app will:
- ✅ Auto-install dependencies (first time only)
- ✅ Start the web server
- ✅ Open your browser automatically

See **HOW_TO_START.md** for detailed instructions.

---

### 🔧 **MANUAL METHOD - For Advanced Users**

1. **Clone or download this project**

```bash
cd ai-timeline-generator
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
python app.py
```

4. **Open in browser**

```
http://localhost:5000
```

## 📖 How to Use

### Step 1: Prepare Your SRT File

Make sure you have an SRT file with your script/subtitles. Format example:

```
1
00:00:01,000 --> 00:00:04,500
Welcome to the mysterious forest

2
00:00:04,500 --> 00:00:08,200
Where ancient secrets await discovery

3
00:00:08,200 --> 00:00:12,000
Our hero begins the journey
```

### Step 2: Upload and Generate

1. Open the web app at `http://localhost:5000`
2. Enter your **OpenAI API key** (get one at https://platform.openai.com/api-keys)
3. Upload your **SRT file**
4. Click **"Generate Timeline"**

### Step 3: Wait for Processing

The system will:
- Parse your SRT file
- Group lines into scenes (1-4 lines per image)
- Analyze script with GPT-4o to detect visual theme
- Generate optimized prompts for each scene
- Create images using HuggingFace (SDXL)
- Build a synced timeline
- Export Premiere Pro XML

**⏱️ Time estimate**: ~2-5 minutes per image (depends on HuggingFace queue)

### Step 4: Import to Premiere Pro

1. Download the generated **XML file**
2. Open **Adobe Premiere Pro**
3. Go to **File → Import**
4. Select the downloaded XML file
5. Your timeline with synced images is ready! 🎉

## 🎨 How It Works

```
SRT File → Parse → Semantic Grouping → GPT-4o Theme Detection
    ↓
GPT-4o Prompt Generation → HuggingFace Image Gen → Timeline Mapping
    ↓
Premiere Pro XML Export
```

### Smart Semantic Grouping

The system intelligently groups subtitle lines based on:
- Sentence structure and punctuation
- Timing gaps between lines
- Maximum 4 lines per image
- Maximum 8 seconds per image

### Theme Detection (GPT-4o)

GPT-4o analyzes your script to determine:
- Art style (cinematic, cartoon, realistic, etc.)
- Mood and atmosphere
- Lighting style
- Color palette
- Visual characteristics

### Prompt Generation (GPT-4o)

For each scene, GPT-4o creates:
- Consistent style with overall theme
- Descriptive visual elements
- Composition details
- Quality tags for SDXL
- Context-aware scene descriptions

### Image Generation (HuggingFace)

Uses free HuggingFace Inference API:
- Model: Stable Diffusion XL (SDXL)
- Resolution: 1024x1024
- Automatic retries if queue is busy
- Fallback placeholders if generation fails

## 🔧 Configuration

### Using HuggingFace Token (Optional)

For faster image generation, add your HuggingFace token:

1. Get token from https://huggingface.co/settings/tokens
2. Edit `utils/image_generator.py`
3. Add token to headers:

```python
headers = {"Authorization": f"Bearer YOUR_HF_TOKEN"}
```

### Adjusting Grouping Parameters

Edit `app.py` to customize semantic grouping:

```python
grouped_segments = group_lines_semantically(
    subtitles,
    max_lines=4,      # Max lines per image
    max_duration=8000  # Max duration in ms
)
```

## 📁 Project Structure

```
ai-timeline-generator/
├── app.py                      # Flask web server
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/
│   └── index.html             # Web interface
├── utils/
│   ├── srt_parser.py          # SRT file parser
│   ├── semantic_grouper.py    # Line grouping logic
│   ├── theme_detector.py      # GPT-4o theme analysis
│   ├── prompt_generator.py    # GPT-4o prompt creation
│   ├── image_generator.py     # HuggingFace image gen
│   └── timeline_exporter.py   # Premiere Pro XML export
├── uploads/                   # Uploaded SRT files
├── outputs/                   # Generated XML files
└── static/
    └── generated_images/      # Generated images
```

## 🐛 Troubleshooting

### "HuggingFace model is loading"

The free tier sometimes has cold starts. Wait 20-30 seconds and it will retry automatically.

### "OpenAI API key invalid"

Make sure you:
1. Created an API key at https://platform.openai.com/api-keys
2. Have billing enabled on your OpenAI account
3. Copied the full key starting with `sk-`

### Images not generating

- Check your internet connection
- HuggingFace free tier has rate limits - add delays between images
- Consider adding a HuggingFace token for priority access

### XML not importing to Premiere Pro

- Make sure image paths are accessible
- Try copying the `generated_images` folder to your project directory
- Update paths in XML if needed

## 🚀 Roadmap / Future Enhancements

- [ ] Support for multiple image generation providers (Replicate, FAL.ai)
- [ ] Character consistency across images
- [ ] Style reference image support
- [ ] DaVinci Resolve timeline export
- [ ] Real-time progress updates via WebSocket
- [ ] Batch processing multiple SRT files
- [ ] Cloud storage integration (Google Drive, Cloudinary)

## 📄 License

Free to use for personal and commercial projects.

## 🙏 Credits

- **GPT-4o** by OpenAI - Theme detection and prompt generation
- **Stable Diffusion XL** by Stability AI - Image generation
- **HuggingFace** - Free inference API
- Built with Flask, Python, and ❤️

## 📧 Support

Having issues? Create an issue or contact support.

---

**Happy Creating! 🎨✨**

