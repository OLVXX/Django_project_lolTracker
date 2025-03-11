import os
import shutil
import sys
from pathlib import Path

def setup_static_files():
    """Create and organize static file directories"""
    # Define base directory
    base_dir = Path(__file__).resolve().parent

    # Create main static directories
    static_dirs = [
        base_dir / 'static' / 'css',
        base_dir / 'static' / 'js',
        base_dir / 'static' / 'img',
        base_dir / 'match_analyzer' / 'analysis' / 'static' / 'analysis' / 'css',
        base_dir / 'match_analyzer' / 'analysis' / 'static' / 'analysis' / 'js',
        base_dir / 'match_analyzer' / 'analysis' / 'static' / 'analysis' / 'img',
    ]

    # Create directories
    for directory in static_dirs:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")

    # Create default CSS file if it doesn't exist
    css_file = base_dir / 'match_analyzer' / 'analysis' / 'static' / 'analysis' / 'css' / 'style.css'
    if not css_file.exists():
        with open(css_file, 'w') as f:
            f.write('/* Default styles for match analyzer */')
        print(f"Created CSS file: {css_file}")
    else:
        print(f"CSS file already exists: {css_file}")

    # Copy static files if analysis/static exists
    analysis_static = base_dir / 'analysis' / 'static'
    if analysis_static.exists():
        target_dir = base_dir / 'static'
        for item in analysis_static.glob('**/*'):
            if item.is_file():
                # Create target directory if it doesn't exist
                relative_path = item.relative_to(analysis_static)
                target_file = target_dir / relative_path
                target_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Copy the file
                shutil.copy2(item, target_file)
                print(f"Copied: {item} -> {target_file}")
    
    print("Static directories setup completed successfully!")

if __name__ == "__main__":
    setup_static_files()
