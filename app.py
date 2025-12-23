from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>Hello World</h1>")

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), HelloHandler)
    print("Server dang chay tai http://localhost:8000")
    server.serve_forever()