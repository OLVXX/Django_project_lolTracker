"""
This script specifically fixes the CSS path issues in the project.
It puts the CSS file in all the locations Django might look for it.
"""

import os
import shutil
import sys
from pathlib import Path

def fix_css_paths():
    # Get the base directory
    base_dir = Path(__file__).resolve().parent
    
    # Define all possible CSS locations
    css_paths = [
        base_dir / 'analysis' / 'static' / 'analysis' / 'css' / 'style.css',
        base_dir / 'static' / 'analysis' / 'css' / 'style.css',
        base_dir / 'staticfiles' / 'analysis' / 'css' / 'style.css',
    ]
    
    # Create simple CSS content
    css_content = """/* Basic styles for the match analyzer */
body {
  font-family: "Arial", sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
  color: #333;
}

.container {
  width: 80%;
  margin: auto;
  overflow: hidden;
  padding: 20px;
}

/* Header styling */
.header {
  background-color: #1a237e;
  color: white;
  padding: 20px 0;
  text-align: center;
}

/* Form styling */
form {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

/* Button styling */
button, input[type="submit"] {
  background: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  font-size: 16px;
}

button:hover, input[type="submit"]:hover {
  background: #45a049;
}

/* Results styling */
.results {
  background: white;
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Match card styling */
.match-card {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 3px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.match-win {
  background-color: #e3f2fd;
  border-left: 5px solid #2196F3;
}

.match-loss {
  background-color: #ffebee;
  border-left: 5px solid #f44336;
}

/* Error message */
.error {
  color: #f44336;
  background-color: #ffebee;
  padding: 10px;
  border-radius: 3px;
  margin-bottom: 15px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .container {
    width: 95%;
  }
}"""
    
    # Create all CSS files and their parent directories
    for css_path in css_paths:
        try:
            # Create parent directories if they don't exist
            css_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Create or overwrite the CSS file
            with open(css_path, 'w') as f:
                f.write(css_content)
            
            print(f"Created or updated CSS at: {css_path}")
        except Exception as e:
            print(f"Error creating {css_path}: {e}")

    # Find all template files that might reference the CSS
    template_paths = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                template_paths.append(os.path.join(root, file))
    
    # Check templates to make sure they properly load static
    for template_path in template_paths:
        try:
            with open(template_path, 'r') as f:
                content = f.read()
            
            # Check if template has proper static loading
            if 'analysis/css/style.css' in content:
                # Template references the CSS
                if '{% load static %}' not in content and '{% load staticfiles %}' not in content:
                    # No static tag - add it at the top
                    content = '{% load static %}\n' + content
                    with open(template_path, 'w') as f:
                        f.write(content)
                    print(f"Added static loading tag to {template_path}")
        except Exception as e:
            print(f"Error checking template {template_path}: {e}")
    
    # Run collectstatic
    try:
        print("\nRunning collectstatic...")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "match_analyzer.settings")
        import django
        django.setup()
        from django.core.management import call_command
        call_command('collectstatic', '--noinput', verbosity=1)
        print("✓ Collectstatic completed successfully")
    except Exception as e:
        print(f"Error running collectstatic: {e}")
        print("Run manually with: python manage.py collectstatic --noinput")

if __name__ == "__main__":
    fix_css_paths()
