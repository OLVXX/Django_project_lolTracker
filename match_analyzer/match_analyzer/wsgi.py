"""
WSGI config for match_analyzer project.
"""

import os
import sys
import logging

print("Starting WSGI script")
print(f"Current directory: {os.getcwd()}")
print(f"Script file: {__file__}")

# Explicitly set the path to include the project
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Base directory: {base_dir}")

# Add all relevant paths
sys.path.insert(0, base_dir)
sys.path.insert(0, os.path.dirname(base_dir))
sys.path.insert(0, os.path.join(base_dir, 'match_analyzer'))

print(f"Python path: {sys.path}")

# Set up the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'match_analyzer.settings')
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("Application created successfully")
except Exception as e:
    print(f"Error creating application: {e}")
    logging.exception("Error in WSGI")
    raise
