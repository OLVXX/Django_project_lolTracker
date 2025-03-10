#!/usr/bin/env bash
# exit on error
set -o errexit

# Debug: Show current directory
echo "Current directory:"
pwd
ls -la

# First upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify the Python module structure
echo "Debugging Python modules:"
python debug.py

# Create static directories based on your repo structure
mkdir -p static
mkdir -p static/analysis/css
mkdir -p staticfiles

# Debug: Check existing static files
echo "Looking for existing CSS files:"
find . -name "*.css" | grep -v "node_modules" | grep -v "venv"

# Copy any existing CSS files to the static directory
for css_file in $(find . -path "*analysis*/static/*css/*.css" | grep -v "node_modules" | grep -v "venv"); do
  echo "Copying CSS file: $css_file"
  mkdir -p $(dirname static/${css_file#*/static/})
  cp $css_file static/${css_file#*/static/}
done

# Create CSS file directly in the static directory if no CSS file exists
if [ ! -f static/analysis/css/style.css ]; then
  echo "Creating CSS file in static directory"
  cat > static/analysis/css/style.css << 'EOL'
/* Basic styles */
body {
  font-family: 'Inter', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa;
  color: #333;
}
.navbar {
  background-color: #6c5ce7;
  padding: 15px 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
/* ... more styles ... */
EOL
fi

# Show static directory structure for debugging
echo "Static directory structure:"
find static -type f | sort
echo "Static directory permissions:"
ls -la static/analysis/css/

# Run Django commands with debugging output
PYTHONVERBOSE=1 python manage.py collectstatic --noinput --verbosity 3
PYTHONVERBOSE=1 python manage.py migrate --verbosity 3

# Debug WSGI file for render
echo "WSGI file content:"
cat match_analyzer/wsgi.py
