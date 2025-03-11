"""
This script checks the build process and ensures collectstatic works properly.
It can be run locally to verify that the build process will work in deployment.
"""
import os
import sys
import subprocess
from pathlib import Path
import shutil

def check_collectstatic():
    """Verify collectstatic works correctly"""
    print("Checking collectstatic process...")
    
    # Get base directory
    base_dir = Path(__file__).resolve().parent
    
    # Check for CSS files in the app static folders
    css_paths = [
        base_dir / 'analysis' / 'static' / 'analysis' / 'css' / 'style.css',
        base_dir / 'static' / 'analysis' / 'css' / 'style.css',
        base_dir / 'staticfiles' / 'analysis' / 'css' / 'style.css',
    ]
    
    # Record initial state
    initial_state = {}
    for path in css_paths:
        initial_state[str(path)] = path.exists()
    
    # Clear staticfiles directory to test collection
    staticfiles_dir = base_dir / 'staticfiles'
    if staticfiles_dir.exists():
        print(f"Clearing {staticfiles_dir} to test collection...")
        shutil.rmtree(staticfiles_dir)
        os.makedirs(staticfiles_dir, exist_ok=True)
    
    # Run collectstatic
    try:
        print("\nRunning collectstatic command...")
        result = subprocess.run(
            [sys.executable, 'manage.py', 'collectstatic', '--noinput', '--verbosity=2'],
            capture_output=True, 
            text=True,
            check=True
        )
        print(result.stdout)
        
        # Check if files were collected properly
        output_file = staticfiles_dir / 'analysis' / 'css' / 'style.css'
        if output_file.exists():
            print(f"✓ CSS collected successfully: {output_file}")
            with open(output_file, 'r') as f:
                content = f.read(100)  # Read just the first 100 chars
                print(f"Content preview: {content}...")
        else:
            print(f"✗ CSS not collected properly. Missing: {output_file}")
            
            # Check if Django found the source files
            print("\nChecking if source files exist:")
            for path in css_paths:
                if path.exists():
                    print(f"✓ Source exists: {path}")
                else:
                    print(f"✗ Source missing: {path}")
            
            # Check Django settings
            check_django_settings()
        
    except subprocess.CalledProcessError as e:
        print(f"Error running collectstatic: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False
    
    return True

def check_django_settings():
    """Check Django static settings"""
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "match_analyzer.settings")
        import django
        django.setup()
        
        from django.conf import settings
        print("\nDjango static settings:")
        print(f"STATIC_URL: {settings.STATIC_URL}")
        print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
        print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
        
        # Check finders
        print("\nStatic finders:")
        for finder in settings.STATICFILES_FINDERS:
            print(f"  - {finder}")
            
        # Check installed apps
        if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
            print("✓ django.contrib.staticfiles is in INSTALLED_APPS")
        else:
            print("✗ django.contrib.staticfiles is NOT in INSTALLED_APPS")
        
        # Check whitenoise
        if 'whitenoise.middleware.WhiteNoiseMiddleware' in settings.MIDDLEWARE:
            print("✓ WhiteNoiseMiddleware is in MIDDLEWARE")
        else:
            print("✗ WhiteNoiseMiddleware is NOT in MIDDLEWARE")
            
    except Exception as e:
        print(f"Error checking Django settings: {e}")

def check_css_in_templates():
    """Check how CSS is referenced in templates"""
    base_dir = Path(__file__).resolve().parent
    
    template_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                template_files.append(os.path.join(root, file))
    
    print(f"\nChecking CSS references in {len(template_files)} template files:")
    
    for template in template_files:
        with open(template, 'r', encoding='utf-8') as f:
            content = f.read()
            
            if 'style.css' in content:
                print(f"\nTemplate: {template}")
                
                if '{% load static %}' in content or '{% load staticfiles %}' in content:
                    print("✓ Has static load tag")
                else:
                    print("✗ Missing static load tag")
                
                if 'href="{% static' in content and 'style.css' in content:
                    print("✓ Using static template tag for CSS")
                    # Extract the pattern
                    import re
                    patterns = re.findall(r'href=[\'"]{1,2}{% static [\'"]([^\'"]+)[\'"] %}[\'"]{1,2}', content)
                    for pattern in patterns:
                        if 'style.css' in pattern:
                            print(f"  CSS path: {pattern}")
                elif 'href="/static/' in content and 'style.css' in content:
                    print("✗ Using hardcoded static path instead of template tag")
                    import re
                    patterns = re.findall(r'href=[\'"]{1,2}/static/([^\'"]+)[\'"]{1,2}', content)
                    for pattern in patterns:
                        if 'style.css' in pattern:
                            print(f"  CSS path: {pattern}")
                else:
                    print("? Unusual CSS reference pattern")

if __name__ == "__main__":
    print("Checking build process for Django static files...")
    
    # Check CSS in templates
    check_css_in_templates()
    
    # Check collectstatic
    successful = check_collectstatic()
    
    if successful:
        print("\n✓ Collectstatic process verified successfully!")
    else:
        print("\n✗ Issues found with collectstatic process.")
        print("Please fix the above issues before deploying.")
