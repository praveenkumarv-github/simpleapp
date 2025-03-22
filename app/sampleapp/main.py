from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os

class SimpleWebAppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.serve_index_html()
        else:
            self.send_error(404, "Page Not Found")

    def serve_index_html(self):
        try:
            # Get server and client information
            server_ip = socket.gethostbyname(socket.gethostname())
            client_ip = self.client_address[0]
            request_method = self.command

            # Read HTML template
            file_path = os.path.join(os.path.dirname(__file__), 'index.html')
            with open(file_path, 'r') as file:
                html_content = file.read()

            # Replace placeholders with dynamic values
            html_content = html_content.replace("{{SERVER_IP}}", server_ip)
            html_content = html_content.replace("{{CLIENT_IP}}", client_ip)
            html_content = html_content.replace("{{REQUEST_METHOD}}", request_method)

            # Send response headers
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Write the updated HTML content
            self.wfile.write(html_content.encode('utf-8'))
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {e}")

def run_web_app(port=80):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleWebAppHandler)
    print(f"Starting web app on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
    finally:
        httpd.server_close()

if __name__ == '__main__':
    run_web_app()
