import http.server
import socketserver
import os
from functools import partial

PORT = int(os.environ.get("PORT", 8000))
UI_DIR = os.path.join(os.path.dirname(__file__), '..', 'ui')

# Ensure the UI directory path is absolute
UI_DIR = os.path.abspath(UI_DIR)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=UI_DIR, **kwargs)

if __name__ == "__main__":
    # Binding to "0.0.0.0" allows external hosting (like Render) to properly route traffic
    with socketserver.TCPServer(("0.0.0.0", PORT), CustomHandler) as httpd:
        print(f"JARVIS UI available at http://0.0.0.0:{PORT}")
        print(f"Serving files from: {UI_DIR}")
        httpd.serve_forever()
        
