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

# Create static directories
mkdir -p static/analysis/css
mkdir -p staticfiles

# Create CSS file directly in the static directory
echo "Creating CSS file in static directory"

cat > static/analysis/css/style.css << 'EOL'
/* Base styles */
body {
  font-family: "Inter", sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa;
  color: #333;
  line-height: 1.6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.navbar {
  background-color: #6c5ce7;
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
  align-items: center;
}

.nav-button {
  background-color: #a29bfe;
  color: #ffffff;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  margin-left: 15px;
  text-decoration: none;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s;
}

.nav-button:hover {
  background-color: #8c7ae6;
}

/* Form styles */
.form-container {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 30px;
  max-width: 500px;
  margin: 30px auto;
}

.form-group {
  margin-bottom: 20px;
}

.welcome-text {
  color: #ffffff;
  margin-right: 15px;
}

/* Basic responsive design */
@media (max-width: 768px) {
  .nav-content {
    flex-direction: column;
  }
  
  .nav-items {
    margin-top: 15px;
  }
}
EOL

echo "Static directory after content creation:"
find static -type f -name "*.css" | xargs ls -la

# Run Django commands
python manage.py collectstatic --noinput --clear
python manage.py migrate
