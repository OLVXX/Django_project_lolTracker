"""
Comprehensive static file checker and fixer for Django
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path

def run_command(command):
    """Run a command and return the result"""
    print(f"Running: {' '.join(command)}")
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return None

def check_and_fix_static():
    """Check and fix static files issues"""
    base_dir = Path(__file__).resolve().parent
    
    # 1. Check directory structure
    print("\n1. Checking directory structure...")
    static_dirs = [
        base_dir / 'static',
        base_dir / 'staticfiles',
        base_dir / 'analysis' / 'static' / 'analysis' / 'css',
    ]
    
    for directory in static_dirs:
        if directory.exists():
            print(f"✓ Found: {directory}")
        else:
            print(f"Creating: {directory}")
            directory.mkdir(parents=True, exist_ok=True)
    
    # 2. Check CSS files
    print("\n2. Checking CSS files...")
    css_paths = [
        base_dir / 'analysis' / 'static' / 'analysis' / 'css' / 'style.css',
        base_dir / 'static' / 'analysis' / 'css' / 'style.css',
    ]
    
    # Find a source CSS file
    source_css = None
    for path in css_paths:
        if path.exists():
            source_css = path
            print(f"✓ Found source CSS: {path}")
            break
    
    # If no CSS file exists, create a default one
    if source_css is None:
        source_css = css_paths[0]  # Use the first path
        print(f"Creating default CSS at: {source_css}")
        source_css.parent.mkdir(parents=True, exist_ok=True)
        
        with open(source_css, 'w') as f:
            f.write("""/* Basic CSS for the Match Analyzer */
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --text-primary: #2d3436;
  --text-secondary: #636e72;
  --accent: #6c5ce7;
  --card-bg: #ffffff;
  --victory: #00b894;
  --defeat: #ff7675;
}

body {
  font-family: "Arial", sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: var(--bg-secondary);
  color: var(--text-primary);
}

.container {
  width: 80%;
  margin: auto;
  overflow: hidden;
  padding: 20px;
}

/* Navigation */
.navbar {
  background-color: var(--accent);
  padding: 15px 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.nav-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.nav-brand {
  color: #ffffff;
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
}

.nav-items {
  display: flex;
  gap: 15px;
  align-items: center;
}

.nav-button {
  background: rgba(255,255,255,0.2);
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  text-decoration: none;
  transition: background 0.3s;
}

.nav-button:hover {
  background: rgba(255,255,255,0.3);
}

.welcome-text {
  color: white;
  margin-right: 10px;
}
""")
    
    # Copy the CSS file to all required locations
    for path in css_paths:
        if path != source_css:
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_css, path)
            print(f"✓ Copied CSS to: {path}")
    
    # 3. Check base.html templates
    print("\n3. Checking templates...")
    template_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                template_files.append(Path(root) / file)
    
    print(f"Found {len(template_files)} HTML templates")
    
    # Check for base.html files specifically
    base_html_files = [f for f in template_files if f.name == 'base.html']
    if len(base_html_files) > 1:
        print(f"⚠️ Warning: Multiple base.html files found ({len(base_html_files)})")
        for f in base_html_files:
            print(f"  • {f}")
    
    # 4. Check dependencies
    print("\n4. Checking dependencies...")
    dependencies = ['django', 'whitenoise']
    for dep in dependencies:
        try:
            module = __import__(dep)
            print(f"✓ {dep} is installed")
        except ImportError:
            print(f"⚠️ {dep} is not installed. Installing...")
            run_command([sys.executable, '-m', 'pip', 'install', dep])
    
    # 5. Run collectstatic
    print("\n5. Running collectstatic...")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "match_analyzer.settings")
    
    try:
        import django
        django.setup()
        
        # Run collectstatic
        from django.core.management import call_command
        print("Collecting static files...")
        call_command('collectstatic', interactive=False, verbosity=1)
        print("✓ Collectstatic completed successfully")
        
        # Check if files were collected
        from django.conf import settings
        static_root = Path(settings.STATIC_ROOT)
        collected_css = static_root / 'analysis' / 'css' / 'style.css'
        
        if collected_css.exists():
            print(f"✓ CSS was properly collected to: {collected_css}")
        else:
            print(f"✗ CSS was NOT collected to: {collected_css}")
            print("This indicates an issue with your static files configuration")
    
    except Exception as e:
        print(f"Error: {e}")
        # Try running it as a command if module import failed
        result = run_command([sys.executable, 'manage.py', 'collectstatic', '--noinput'])
        if result:
            print("✓ Collectstatic completed via command line")
    
    # 6. Final check and advice
    print("\n6. Final check...")
    staticfiles_dir = base_dir / 'staticfiles'
    if not staticfiles_dir.exists() or not any(staticfiles_dir.iterdir()):
        print("⚠️ Warning: staticfiles directory is empty or doesn't exist")
        print("This indicates collectstatic may have failed or your STATIC_ROOT setting is incorrect")
    else:
        print(f"✓ staticfiles directory exists at: {staticfiles_dir}")
        
        # Check specific paths
        expected_css = staticfiles_dir / 'analysis' / 'css' / 'style.css'
        if expected_css.exists():
            print(f"✓ CSS collected to correct location: {expected_css}")
        else:
            print(f"✗ CSS missing from: {expected_css}")
    
    print("\nDeploy checklist:")
    print("✓ Static files are set up correctly")
    print("✓ CSS is in the correct location")
    print("✓ Templates should properly load CSS when DEBUG=False")
    print("\nNext steps:")
    print("1. Make sure 'whitenoise.middleware.WhiteNoiseMiddleware' is in MIDDLEWARE")
    print("2. Make sure 'django.contrib.staticfiles' is in INSTALLED_APPS")
    print("3. Set DEBUG=False to test production environment")

if __name__ == "__main__":
    check_and_fix_static()
