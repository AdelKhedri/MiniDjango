from http.server import BaseHTTPRequestHandler, HTTPServer
from ....urls import routes
import sys
from ....utils.colors import Colors
from datetime import datetime


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path[1:]

        if path in routes:
            response = routes[path]
            if callable(response):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                response = response(self.request)
            else:
                sys.exit('{}view must be a function{}'.format(Colors.RED, Colors.RESET))
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Page not found.')



def runserver():
    server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    text = f'{datetime.now()} \nMiniDjango version 1.0.0 \nStarting development server at http://127.0.0.1:8000 \nQuit the server with CONTROL+C \n\n'
    sys.stdout.write(text)
    server.serve_forever()
