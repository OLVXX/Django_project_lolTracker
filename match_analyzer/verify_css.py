"""
This script verifies that CSS files exist and are accessible.
It also checks for multiple base.html files that might cause conflicts.
"""
import os
from pathlib import Path
import requests
import webbrowser
import http.server
import socketserver
import threading
import time

def find_duplicate_templates():
    """Find any duplicate base.html files in the project"""
    base_dir = Path(__file__).resolve().parent
    base_html_files = []
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file == 'base.html':
                path = Path(root) / file
                base_html_files.append(str(path))
    
    if len(base_html_files) > 1:
        print("⚠️ Warning: Multiple base.html files found:")
        for path in base_html_files:
            print(f"  • {path}")
        print("\nThis may cause templates to extend the wrong base file.")
    else:
        print("✓ No duplicate base.html files found.")
    
    return base_html_files

def verify_css_files():
    """Verify CSS files exist in the correct locations"""
    base_dir = Path(__file__).resolve().parent
    
    # Locations to check
    css_locations = [
        base_dir / 'analysis' / 'static' / 'analysis' / 'css' / 'style.css',
        base_dir / 'static' / 'analysis' / 'css' / 'style.css',
        base_dir / 'staticfiles' / 'analysis' / 'css' / 'style.css',
    ]
    
    all_exist = True
    print("\nChecking CSS files:")
    for loc in css_locations:
        if loc.exists():
            print(f"✓ Found: {loc}")
        else:
            print(f"✗ Missing: {loc}")
            all_exist = False
    
    if not all_exist:
        print("\nSome CSS files are missing. Run:")
        print("python fix_css_paths.py")
        print("python manage.py collectstatic --noinput")

def start_test_server(port=8000):
    """Start a simple HTTP server to test static files"""
    base_dir = Path(__file__).resolve().parent
    
    # Use staticfiles directory if it exists, otherwise use static
    if (base_dir / 'staticfiles').exists():
        os.chdir(base_dir / 'staticfiles')
        print(f"\nStarting test server for staticfiles directory on port {port}...")
    elif (base_dir / 'static').exists():
        os.chdir(base_dir / 'static')
        print(f"\nStarting test server for static directory on port {port}...")
    else:
        print("No static directories found to serve.")
        return
    
    # Start server in a separate thread
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Try to access CSS file
    time.sleep(1)  # Give server time to start
    
    try:
        css_url = f"http://localhost:{port}/analysis/css/style.css"
        response = requests.get(css_url)
        
        if response.status_code == 200:
            print(f"✓ CSS file accessible at: {css_url}")
            print("CSS content preview:")
            print("-" * 40)
            print(response.text[:200] + "..." if len(response.text) > 200 else response.text)
            print("-" * 40)
            
            # Open in browser
            webbrowser.open(css_url)
        else:
            print(f"✗ Failed to access CSS file. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error accessing CSS: {e}")
    
    # Shutdown server
    print("\nPress Ctrl+C to stop the server when finished testing.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        httpd.shutdown()
        print("Server stopped.")

if __name__ == "__main__":
    find_duplicate_templates()
    verify_css_files()
    start_test_server()
