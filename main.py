import http.server
import socketserver
import os

PORT = 8000
UI_DIR = os.path.join(os.path.dirname(__file__), '..', 'ui')

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=UI_DIR, **kwargs)

            if __name__ == "__main__":
                with socketserver.TCPServer(("", PORT), Handler) as httpd:
                        print(f"JARVIS UI available at http://localhost:{PORT}")
                                httpd.serve_forever()
                                