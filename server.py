import json
from http.server import BaseHTTPRequestHandler, HTTPServer

NOTES = [{"id": 1, "text": "Review HTTP status codes"}]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/notes":
            body = json.dumps(NOTES).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_error(404)

if __name__ == "__main__":
    print("Listening on http://127.0.0.1:8000/notes")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
