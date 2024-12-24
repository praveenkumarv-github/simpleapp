from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleWebAppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Read HTML content from file
        file_path = os.path.join(os.path.dirname(__file__), 'index.html')
        with open(file_path, 'r') as file:
            html_content = file.read()

        self.wfile.write(html_content.encode('utf-8'))

def run_web_app(port=80):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleWebAppHandler)
    print('Starting web app on port {}'.format(port))
    httpd.serve_forever()

if __name__ == '__main__':
    run_web_app()