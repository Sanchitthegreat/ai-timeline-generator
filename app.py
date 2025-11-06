from flask import Flask, render_template, request, jsonify, send_file
import os
import json
import base64
from pathlib import Path
from utils.srt_parser import parse_srt
from utils.semantic_grouper import group_lines_semantically
from utils.theme_detector import detect_theme
from utils.prompt_generator import generate_image_prompts
from utils.image_generator import generate_images
from utils.replicate_generator import generate_images_replicate
from utils.local_drawatoon_generator import generate_images_local_drawatoon
from utils.timeline_exporter import export_premiere_xml

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
os.makedirs('static/generated_images', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/detect-theme', methods=['POST'])
def detect_theme_only():
    """Step 1: Parse SRT, group segments, and detect theme for user approval"""
    try:
        # Get API keys from request
        api_key = request.form.get('api_key')
        if not api_key:
            return jsonify({'error': 'OpenAI API key is required'}), 400
        
        # Get uploaded SRT file
        if 'srt_file' not in request.files:
            return jsonify({'error': 'No SRT file uploaded'}), 400
        
        srt_file = request.files['srt_file']
        if srt_file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save uploaded file
        srt_path = os.path.join(app.config['UPLOAD_FOLDER'], srt_file.filename)
        srt_file.save(srt_path)
        
        # Parse SRT file
        print("📄 Parsing SRT file...")
        subtitles = parse_srt(srt_path)
        
        # Group lines semantically
        print("🧩 Grouping lines semantically...")
        grouped_segments = group_lines_semantically(subtitles)
        
        # Get manga mode and aspect ratio settings
        manga_mode = request.form.get('manga_mode', 'false') == 'true'
        aspect_ratio = request.form.get('aspect_ratio', '16:9')
        
        # Detect overall theme using GPT-4o
        print("🎨 Detecting theme with GPT-4o...")
        theme = detect_theme(grouped_segments, api_key, manga_mode, aspect_ratio)
        
        # Store grouped segments for later use
        import json
        session_id = Path(srt_file.filename).stem
        session_file = os.path.join(app.config['UPLOAD_FOLDER'], f'{session_id}_data.json')
        with open(session_file, 'w') as f:
            json.dump({
                'theme': theme,
                'grouped_segments': grouped_segments,
                'srt_filename': srt_file.filename,
                'manga_mode': manga_mode,
                'aspect_ratio': aspect_ratio
            }, f)
        
        return jsonify({
            'success': True,
            'theme': theme,
            'total_segments': len(grouped_segments),
            'session_id': session_id
        })
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate-prompts', methods=['POST'])
def generate_prompts_only():
    """Step 2: Generate prompts using approved theme"""
    try:
        # Get API key and approved theme from request
        data = request.get_json()
        api_key = data.get('api_key')
        approved_theme = data.get('approved_theme')
        session_id = data.get('session_id')
        manga_mode = data.get('manga_mode', 'false') == 'true'
        aspect_ratio = data.get('aspect_ratio', '16:9')
        
        if not api_key:
            return jsonify({'error': 'OpenAI API key is required'}), 400
        if not approved_theme:
            return jsonify({'error': 'Approved theme is required'}), 400
        if not session_id:
            return jsonify({'error': 'Session ID is required'}), 400
        
        # Load session data
        import json
        session_file = os.path.join(app.config['UPLOAD_FOLDER'], f'{session_id}_data.json')
        
        if not os.path.exists(session_file):
            return jsonify({'error': 'Session expired or not found'}), 404
        
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        grouped_segments = session_data['grouped_segments']
        
        # Update manga mode and aspect ratio in session if changed
        session_data['manga_mode'] = manga_mode
        session_data['aspect_ratio'] = aspect_ratio
        
        # Generate prompts for each segment using approved theme
        print("✍️ Generating image prompts with GPT-4o using approved theme...")
        prompts = generate_image_prompts(grouped_segments, approved_theme, api_key, manga_mode, aspect_ratio)
        
        # Update session file with prompts
        session_data['theme'] = approved_theme
        session_data['prompts'] = prompts
        with open(session_file, 'w') as f:
            json.dump(session_data, f)
        
        # Also save to prompts file for backward compatibility
        prompts_file = os.path.join(app.config['UPLOAD_FOLDER'], f'{session_id}_prompts.json')
        with open(prompts_file, 'w') as f:
            json.dump({
                'theme': approved_theme,
                'prompts': prompts,
                'srt_filename': session_data['srt_filename'],
                'aspect_ratio': aspect_ratio,
                'manga_mode': manga_mode
            }, f)
        
        return jsonify({
            'success': True,
            'theme': approved_theme,
            'total_prompts': len(prompts),
            'prompts': [
                {
                    'index': i + 1,
                    'start': seg['start_time'],
                    'end': seg['end_time'],
                    'text': seg['text'],
                    'prompt': seg['prompt']
                }
                for i, seg in enumerate(prompts)
            ],
            'session_id': session_id
        })
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate-images', methods=['POST'])
def generate_images_from_prompts():
    """Step 3: Generate images after user approves prompts"""
    try:
        data = request.get_json()
        session_id = data.get('session_id')
        replicate_token = data.get('replicate_token')
        model_type = data.get('model_type', 'replicate')  # 'replicate' or 'local_drawatoon'
        
        if not session_id:
            return jsonify({'error': 'Session ID required'}), 400
        
        # Load prompts from session - try prompts.json first, then data.json
        import json
        session_file = os.path.join(app.config['UPLOAD_FOLDER'], f'{session_id}_prompts.json')
        
        # If prompts.json doesn't exist, try data.json
        if not os.path.exists(session_file):
            session_file = os.path.join(app.config['UPLOAD_FOLDER'], f'{session_id}_data.json')
        
        if not os.path.exists(session_file):
            return jsonify({'error': 'Session expired or not found'}), 404
        
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        theme = session_data['theme']
        prompts = session_data['prompts']
        aspect_ratio = session_data.get('aspect_ratio', '16:9')  # Default to 16:9 if not found
        
        # Debug: Print aspect ratio being used
        print(f"📐 Using aspect ratio: {aspect_ratio}")
        
        # Generate images based on selected model
        if model_type == 'local_drawatoon':
            if not replicate_token:  # We don't need it, but check for consistency
                pass
            print("🎨 Generating images with Local Drawatoon-v1 (manga style, free)...")
            images = generate_images_local_drawatoon(prompts, aspect_ratio)
        else:  # Default to Replicate
            if not replicate_token:
                return jsonify({'error': 'Replicate API token required'}), 400
            print("🎨 Generating images with Replicate FLUX (fast & high quality)...")
            images = generate_images_replicate(prompts, replicate_token, aspect_ratio)
        
        # Export Premiere Pro XML
        print("📦 Creating Premiere Pro XML...")
        project_name = session_id
        xml_path = export_premiere_xml(images, project_name, app.config['OUTPUT_FOLDER'])
        
        return jsonify({
            'success': True,
            'theme': theme,
            'total_images': len(images),
            'segments': [
                {
                    'start': seg['start_time'],
                    'end': seg['end_time'],
                    'text': seg['text'],
                    'prompt': seg['prompt'],
                    'image': seg['image_path']
                }
                for seg in images
            ],
            'xml_file': xml_path,
            'download_url': f'/api/download/{os.path.basename(xml_path)}'
        })
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)

@app.route('/api/status')
def status():
    return jsonify({'status': 'ready'})

if __name__ == '__main__':
    # Debug=False to prevent auto-reload during long image generation
    app.run(debug=False, host='0.0.0.0', port=5560)

