#!/usr/bin/env python3
"""
Simple test script for Drawatoon-v1 model
Direct prompt se image generate karega
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

def test_drawatoon_model():
    """Test Drawatoon model with a simple prompt"""
    
    print("🎨 Drawatoon-v1 Model Test")
    print("=" * 50)
    
    # Import the generator
    try:
        from utils.local_drawatoon_generator import generate_images_local_drawatoon
    except ImportError as e:
        print(f"❌ Error importing: {e}")
        print("\nMake sure you're running from the project directory:")
        print("  cd /Users/sanchitchopra/ai-timeline-generator")
        print("  source venv/bin/activate")
        print("  python test_drawatoon.py")
        return
    
    # Simple test prompt
    test_prompt = input("\n📝 Enter your prompt (or press Enter for default): ").strip()
    if not test_prompt:
        test_prompt = "a beautiful anime style character, manga art style, detailed, high quality"
    
    print(f"\n🎯 Prompt: {test_prompt}")
    print("\n⏳ Generating image... (This will take 2-3 minutes)")
    print("   Please wait...\n")
    
    # Create test segment
    test_segment = [{
        'prompt': test_prompt,
        'start_time': '00:00:00',
        'end_time': '00:00:05',
        'text': 'Test image'
    }]
    
    try:
        # Generate image
        results = generate_images_local_drawatoon(
            test_segment,
            output_dir='test_outputs'
        )
        
        if results and len(results) > 0:
            image_path = results[0]['image_path']
            print(f"\n✅ SUCCESS!")
            print(f"📁 Image saved to: {image_path}")
            print(f"\n💡 To view the image:")
            print(f"   open {image_path}")
            print(f"\n   Or check the 'test_outputs' folder")
        else:
            print("\n❌ No image generated")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_drawatoon_model()


