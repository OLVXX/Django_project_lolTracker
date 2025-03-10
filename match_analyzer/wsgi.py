"""
Root-level WSGI file to help Render find the application
"""
import os
import sys

# Add the project directory to the Python path
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path)

# Import the WSGI application from the match_analyzer module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'match_analyzer.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
