"""
This utility checks and fixes CSS paths to ensure they're in the correct locations
and the project can find them.
"""
import os
import shutil
from pathlib import Path

def check_css_paths():
    """Check and fix CSS path issues"""
    base_dir = Path(__file__).resolve().parent
    css_filename = "style.css"
    
    # These are all the possible locations where Django might look for the CSS
    css_locations = {
        "app_static": base_dir / 'analysis' / 'static' / 'analysis' / 'css' / css_filename,
        "project_static": base_dir / 'static' / 'analysis' / 'css' / css_filename,
        "collected_static": base_dir / 'staticfiles' / 'analysis' / 'css' / css_filename,
        "match_analyzer_static": base_dir / 'match_analyzer' / 'static' / 'analysis' / 'css' / css_filename
    }
    
    # Check which locations exist
    print("Checking CSS locations:")
    css_files_found = []
    for name, path in css_locations.items():
        if path.exists():
            print(f"✓ Found CSS at {name}: {path}")
            css_files_found.append(path)
        else:
            print(f"✗ CSS not found at {name}: {path}")
    
    # If no CSS files found, create a basic one
    if not css_files_found:
        print("\nNo CSS files found. Creating a basic one...")
        # Create the primary CSS file in the app's static directory
        primary_css = css_locations["app_static"] 
        primary_css.parent.mkdir(parents=True, exist_ok=True)
        
        with open(primary_css, 'w') as f:
            f.write("""/* Basic CSS for Match Analyzer */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}
""")
        print(f"✓ Created CSS at: {primary_css}")
        css_files_found.append(primary_css)
    
    # Use the first found CSS file as the source to copy to other locations
    source_css = css_files_found[0]
    print(f"\nUsing {source_css} as the source CSS")
    
    # Copy to all other locations
    for name, path in css_locations.items():
        if path != source_css:
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_css, path)
            print(f"✓ Copied CSS to {name}: {path}")
    
    print("\nCSS files are now in sync across all locations.")
    print("\nRunning collectstatic would help ensure CSS is in the staticfiles directory.")
    print("Command: python manage.py collectstatic --noinput")

def get_django_settings():
    """Get Django settings related to static files"""
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "match_analyzer.settings")
        import django
        django.setup()
        
        from django.conf import settings
        
        print("\nDjango Static Settings:")
        print(f"STATIC_URL: {settings.STATIC_URL}")
        print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
        print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
        
        try:
            print(f"STATICFILES_FINDERS: {settings.STATICFILES_FINDERS}")
        except:
            print("STATICFILES_FINDERS: Not explicitly defined (using defaults)")
        
    except Exception as e:
        print(f"Error importing Django settings: {e}")

if __name__ == "__main__":
    # First show settings
    get_django_settings()
    
    # Then check and fix CSS paths
    check_css_paths()
    
    # Try to run collectstatic
    try:
        print("\nAttempting to run collectstatic...")
        import django
        from django.core.management import call_command
        call_command('collectstatic', interactive=False, verbosity=1)
        print("✓ Collectstatic completed successfully!")
    except Exception as e:
        print(f"\nError running collectstatic: {e}")
        print("Please run it manually: python manage.py collectstatic --noinput")
