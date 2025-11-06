# 📖 Complete Usage Guide

## Quick Start (5 Minutes)

### 1️⃣ Setup

**On Mac/Linux:**
```bash
cd ai-timeline-generator
chmod +x run.sh
./run.sh
```

**On Windows:**
```cmd
cd ai-timeline-generator
run.bat
```

**Or manually:**
```bash
pip install -r requirements.txt
python app.py
```

### 2️⃣ Get Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Click **"Create new secret key"**
3. Copy the key (starts with `sk-`)
4. **IMPORTANT**: Add billing/credits to your OpenAI account

### 3️⃣ Open the Web App

Open in your browser:
```
http://localhost:5000
```

### 4️⃣ Generate Your Timeline

1. **Paste your OpenAI API key** in the input field
2. **Upload your SRT file** (or use `example_script.srt` for testing)
3. Click **"Generate Timeline"**
4. Wait for processing (2-5 minutes per image)
5. Download the **Premiere Pro XML file**

---

## 📄 SRT File Format

Your SRT file should look like this:

```srt
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

**Rules:**
- Each subtitle has an index number
- Time format: `HH:MM:SS,mmm --> HH:MM:SS,mmm`
- Text can be multiple lines
- Blank line between subtitles

---

## 🎬 Importing to Premiere Pro

### Method 1: Direct Import

1. Open Adobe Premiere Pro
2. Go to **File → Import**
3. Select the downloaded `.xml` file
4. Your timeline with images will appear!

### Method 2: Manual Import

If direct import doesn't work:

1. Create a new sequence in Premiere Pro
2. Import all images from `static/generated_images/`
3. Drag images to timeline in order
4. Adjust duration to match timestamps (refer to the JSON preview in the web app)

---

## 🎨 Understanding the Process

### Phase 1: Parsing (5 seconds)
- Reads your SRT file
- Extracts timestamps and text

### Phase 2: Semantic Grouping (10 seconds)
- Groups 1-4 subtitle lines together
- Based on context, punctuation, and timing
- Each group = one image

### Phase 3: Theme Detection (30 seconds)
- GPT-4o analyzes your entire script
- Determines visual style, mood, atmosphere
- Creates consistent theme for all images

**Example themes:**
- *"Cinematic fantasy with moody atmospheric lighting, dark color palette with blue accents, mysterious ambiance, film grain"*
- *"Bright cheerful cartoon style, vibrant colors, playful composition, child-friendly aesthetic"*

### Phase 4: Prompt Generation (1-2 minutes)
- GPT-4o creates optimized prompt for each scene
- Maintains consistency with global theme
- Adds quality tags for SDXL

**Example prompts:**
```
Original text: "In the depths of an ancient forest where sunlight barely touches the ground"

Generated prompt: "Ancient mystical forest interior, dappled sunlight filtering through dense canopy, mossy ground, atmospheric fog, cinematic composition, moody lighting with blue tones, mysterious ambiance, detailed environment, 8k quality, SDXL masterpiece"
```

### Phase 5: Image Generation (2-5 minutes per image)
- HuggingFace generates each image
- Uses Stable Diffusion XL
- May queue if API is busy (free tier)
- Automatic retries on failure

### Phase 6: Timeline Export (10 seconds)
- Maps each image to SRT timestamps
- Creates Premiere Pro XML
- Links image files with timeline positions

---

## 💰 Cost Breakdown

**For a 100-image project:**

| Service | Cost | Notes |
|---------|------|-------|
| GPT-4o (theme) | $0.01 | One call to analyze script |
| GPT-4o (prompts) | $0.20 | 100 calls for image prompts |
| HuggingFace | $0.00 | FREE! |
| **TOTAL** | **$0.21** | Super affordable! |

**Typical script lengths:**
- 5 minute video = 40-50 images = ~$0.10
- 10 minute video = 80-100 images = ~$0.20
- 30 minute video = 250-300 images = ~$0.60

---

## ⚙️ Advanced Configuration

### Customize Grouping Logic

Edit `app.py`, line with `group_lines_semantically`:

```python
grouped_segments = group_lines_semantically(
    subtitles,
    max_lines=4,        # Change to 2-6 lines per image
    max_duration=8000   # Change duration (ms)
)
```

**Examples:**
- `max_lines=2` = More images, faster pacing
- `max_lines=6` = Fewer images, longer scenes
- `max_duration=5000` = 5 second max per image

### Add HuggingFace Token (Recommended!)

Get faster image generation:

1. Create free account at https://huggingface.co
2. Get token from https://huggingface.co/settings/tokens
3. Edit `utils/image_generator.py`
4. Update line 31:

```python
headers = {"Authorization": f"Bearer YOUR_HF_TOKEN_HERE"}
```

**Benefits:**
- Faster queue priority
- More reliable generation
- Better rate limits

### Change GPT Model

Edit these files to use different models:

**`utils/theme_detector.py`** (line 29):
```python
model="gpt-4o-mini",  # Cheaper: $0.15 vs $2.50 per 1M tokens
```

**`utils/prompt_generator.py`** (line 41):
```python
model="gpt-3.5-turbo",  # Even cheaper but lower quality
```

---

## 🐛 Common Issues & Solutions

### Issue: "Model is loading" (HuggingFace)

**Solution**: Wait 30 seconds. Free tier has cold starts.

### Issue: "OpenAI API key invalid"

**Solutions**:
- Make sure billing is enabled on OpenAI account
- Check you copied the full key (`sk-...`)
- Verify key hasn't expired

### Issue: Images are low quality

**Solutions**:
- Add HuggingFace token for better processing
- Use GPT-4o instead of GPT-4o-mini for better prompts
- Increase `num_inference_steps` in `image_generator.py` (line 92)

### Issue: Images don't match script

**Solutions**:
- Check if theme detection is accurate
- Manually provide style in the prompt
- Increase GPT temperature for more creativity

### Issue: Processing is very slow

**Reasons**:
- HuggingFace free tier can be slow during peak hours
- Large scripts take longer
- Rate limiting

**Solutions**:
- Add HuggingFace token
- Process during off-peak hours
- Consider paid services (Replicate, FAL.ai)

### Issue: XML won't import to Premiere

**Solutions**:
- Make sure images exist in `static/generated_images/`
- Use absolute paths in XML
- Try copying images to your Premiere project folder

---

## 📊 Expected Results

### Small Script (2-3 minutes, ~20-30 images)
- Processing time: 10-20 minutes
- Cost: ~$0.05
- Quality: Consistent theme, decent images

### Medium Script (10-15 minutes, ~80-100 images)
- Processing time: 40-60 minutes
- Cost: ~$0.20
- Quality: Very consistent, professional

### Large Script (30+ minutes, 250+ images)
- Processing time: 2-3 hours
- Cost: ~$0.60
- Quality: Feature-film ready timeline

---

## 🎯 Pro Tips

### 1. Write Better Scripts
- Be descriptive with visuals
- Mention specific settings, characters, actions
- Use vivid language

**Bad**: "He walks"
**Good**: "The lone traveler walks through the misty mountains at dawn"

### 2. Test First
- Use `example_script.srt` first
- Generate 5-10 images to check theme
- Adjust script if needed

### 3. Theme Override
If you want a specific style, add it to the first subtitle:

```srt
1
00:00:00,000 --> 00:00:01,000
[Style: Anime, vibrant colors, Studio Ghibli inspired]

2
00:00:01,000 --> 00:00:04,500
The adventure begins in a magical world
```

### 4. Character Consistency
For better character consistency:
- Describe characters in detail early
- Use specific names ("the red-haired warrior")
- Keep descriptions consistent throughout

### 5. Batch Processing
- Process multiple scripts overnight
- Use different themes for variety
- Build a library of generated images

---

## 🚀 Next Steps

### Upgrade Options

**Option 1: Better Images ($)**
- Use Replicate API instead of HuggingFace
- Cost: $0.005-0.01 per image
- Benefit: 5-10x faster, better quality, FLUX models

**Option 2: Character Consistency ($$$)**
- Train custom LoRA for characters
- Cost: $1-5 per project
- Benefit: Same character across all images

**Option 3: Custom Styles**
- Upload reference images
- Use ControlNet/IP-Adapter
- Benefit: Match your existing brand/style

### Community

- Share your projects!
- Report bugs and issues
- Suggest improvements

---

## 📧 Need Help?

Check out:
- README.md for installation issues
- This guide for usage questions
- GitHub issues for bug reports

**Happy creating! 🎨✨**

