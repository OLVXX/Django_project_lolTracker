"""
Setup script that installs dependencies and fixes static files
"""

import subprocess
import sys
import os
from pathlib import Path

def setup():
    print("Setting up Match Analyzer project...")
    
    # Get base directory
    base_dir = Path(__file__).resolve().parent
    
    # Install requirements
    print("\n1. Installing dependencies...")
    requirements = [
        "django>=4.2,<5.0", 
        "whitenoise>=6.5.0", 
        "python-dotenv>=1.0.0", 
        "requests>=2.31.0"
    ]
    
    for req in requirements:
        try:
            print(f"Installing {req}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", req])
            print(f"✓ {req} installed successfully")
        except Exception as e:
            print(f"Failed to install {req}: {e}")
    
    # Fix static files
    print("\n2. Setting up static files...")
    try:
        fix_script = base_dir / "fix_static_issue.py"
        if fix_script.exists():
            subprocess.check_call([sys.executable, str(fix_script)])
        else:
            print(f"✗ Fix script not found: {fix_script}")
    except Exception as e:
        print(f"Error running fix_static_issue.py: {e}")
    
    # Run collectstatic
    print("\n3. Running collectstatic...")
    try:
        subprocess.check_call([sys.executable, "manage.py", "collectstatic", "--noinput"])
        print("✓ Static files collected successfully")
    except Exception as e:
        print(f"Error running collectstatic: {e}")
    
    print("\nSetup completed. You can now run the server with:")
    print("python manage.py runserver")

if __name__ == "__main__":
    setup()
