#!/usr/bin/env python
import os
import sys
import importlib
import traceback

def debug_imports():
    """Debug import paths and modules"""
    print("\nPYTHON INFO:")
    print(f"Python version: {sys.version}")
    print(f"Executable path: {sys.executable}")
    
    print("\nCURRENT DIRECTORY:")
    print(os.getcwd())
    
    print("\nSYS.PATH:")
    for p in sys.path:
        print(f"  {p}")
    
    print("\nENVIRONMENT:")
    django_settings = os.environ.get('DJANGO_SETTINGS_MODULE')
    print(f"DJANGO_SETTINGS_MODULE: {django_settings}")
    
    print("\nTESTING IMPORTS:")
    modules_to_test = [
        'django', 
        'match_analyzer', 
        'match_analyzer.settings', 
        'match_analyzer.wsgi'
    ]
    
    for module in modules_to_test:
        try:
            imported = importlib.import_module(module)
            print(f"✓ Successfully imported: {module}")
            if module == 'match_analyzer.wsgi':
                print(f"  wsgi.py path: {imported.__file__}")
                if hasattr(imported, 'application'):
                    print("  'application' attribute exists")
                else:
                    print("  'application' attribute NOT FOUND")
        except Exception as e:
            print(f"✗ Failed to import: {module}")
            print(f"  Error: {str(e)}")
            traceback.print_exc()

if __name__ == "__main__":
    debug_imports()
