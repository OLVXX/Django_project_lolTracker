"""
This script verifies that the static files are set up correctly.
"""

import os
from pathlib import Path
import sys

def verify_static_setup():
    """Verify static files are set up correctly"""
    print("Verifying static file setup...")
    
    # Get the base directory
    base_dir = Path(__file__).resolve().parent
    
    # Define paths to check
    paths_to_check = [
        base_dir / 'analysis' / 'static' / 'analysis' / 'css' / 'style.css',
        base_dir / 'static' / 'analysis' / 'css' / 'style.css',
        base_dir / 'staticfiles' / 'analysis' / 'css' / 'style.css',
    ]
    
    found_count = 0
    missing_count = 0
    
    for path in paths_to_check:
        if path.exists():
            print(f"✓ Found: {path}")
            found_count += 1
        else:
            print(f"✗ Missing: {path}")
            missing_count += 1
    
    print(f"\nSummary: {found_count} CSS files found, {missing_count} missing")
    
    # Check Django settings
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "match_analyzer.settings")
        import django
        django.setup()
        
        from django.conf import settings
        
        print("\nDjango Static Settings:")
        print(f"STATIC_URL: {settings.STATIC_URL}")
        print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
        print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
        
        # Check if staticfiles app is installed
        if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
            print("✓ django.contrib.staticfiles is in INSTALLED_APPS")
        else:
            print("✗ django.contrib.staticfiles is NOT in INSTALLED_APPS")
            
        # Check if whitenoise is installed
        if 'whitenoise' in sys.modules:
            print("✓ Whitenoise is installed")
            
            # Check whitenoise middleware
            if 'whitenoise.middleware.WhiteNoiseMiddleware' in settings.MIDDLEWARE:
                print("✓ WhiteNoiseMiddleware is in MIDDLEWARE")
            else:
                print("✗ WhiteNoiseMiddleware is NOT in MIDDLEWARE")
        else:
            print("✗ Whitenoise is NOT installed")
            
    except Exception as e:
        print(f"Error checking Django settings: {e}")
    
    # If staticfiles directory exists but is empty
    staticfiles_dir = base_dir / 'staticfiles'
    if staticfiles_dir.exists() and not any(staticfiles_dir.iterdir()):
        print("\nWarning: staticfiles directory exists but is empty. Run collectstatic.")
    
    print("\nIf your CSS files are missing, run:")
    print("python fix_css_paths.py")
    print("python manage.py collectstatic --noinput")

if __name__ == "__main__":
    verify_static_setup()
