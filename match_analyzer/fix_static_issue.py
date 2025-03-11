"""
This script fixes the static file paths for the match_analyzer project
"""

import os
import shutil
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import whitenoise
        print("✓ Whitenoise is installed")
    except ImportError:
        print("✗ Whitenoise is not installed. Installing...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "whitenoise"])
            print("✓ Whitenoise installed successfully")
        except Exception as e:
            print(f"Failed to install whitenoise: {e}")
            print("Please install it manually with: pip install whitenoise")
            return False
    return True

def fix_static_paths():
    # Check dependencies first
    if not check_dependencies():
        return
    
    # Get the base directory
    base_dir = Path(__file__).resolve().parent
    
    # Define paths
    analysis_app_dir = base_dir / 'analysis'
    css_source_path = base_dir / 'match_analyzer' / 'analysis' / 'static' / 'analysis' / 'css' / 'style.css'
    css_destination_path = analysis_app_dir / 'static' / 'analysis' / 'css'
    
    # Create the destination directory if it doesn't exist
    css_destination_path.mkdir(parents=True, exist_ok=True)
    
    # If source exists, copy it
    if css_source_path.exists():
        shutil.copy2(css_source_path, css_destination_path / 'style.css')
        print(f"Copied CSS from {css_source_path} to {css_destination_path}")
    else:
        # Create directory structure and default CSS file
        print(f"Source file {css_source_path} not found, creating default CSS...")
        css_destination_file = css_destination_path / 'style.css'
        
        with open(css_destination_file, 'w') as f:
            f.write('/* Default styles for match analyzer */\n')
            f.write('body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }\n')
            f.write('.container { width: 80%; margin: auto; }\n')
        
        print(f"Created default CSS at {css_destination_file}")
        
        # Also create in the expected location if it exists
        if os.path.dirname(css_source_path):
            os.makedirs(os.path.dirname(css_source_path), exist_ok=True)
            shutil.copy2(css_destination_file, css_source_path)
            print(f"Also copied to {css_source_path}")
    
    # Also copy to static root for good measure
    static_css_path = base_dir / 'static' / 'analysis' / 'css'
    static_css_path.mkdir(parents=True, exist_ok=True)
    shutil.copy2(css_destination_path / 'style.css', static_css_path / 'style.css')
    print(f"Copied CSS to {static_css_path}")
    
    print("\nStatic files fixed. Now run collectstatic:")
    print("python manage.py collectstatic --noinput")
    
    # Try to run collectstatic automatically
    try:
        print("\nAttempting to run collectstatic automatically...")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "match_analyzer.settings")
        import django
        django.setup()
        from django.core.management import call_command
        call_command('collectstatic', interactive=False, verbosity=1)
        print("✓ Collectstatic completed successfully")
    except Exception as e:
        print(f"Could not run collectstatic automatically: {e}")
        print("Please run it manually with: python manage.py collectstatic --noinput")

if __name__ == "__main__":
    fix_static_paths()
