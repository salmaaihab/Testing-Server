# Python 3.x
from http.server import BaseHTTPRequestHandler, HTTPServer
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    print(f'Running server on {server_address[0]}:{server_address[1]}...')
    httpd.serve_forever()

run()
