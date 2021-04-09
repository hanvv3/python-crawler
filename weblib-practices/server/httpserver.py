from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

port = 8880


# request가 들어오면 처리하는 RequestHandler
class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        result = urlparse(self.path)
        if result.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('<h1>메인 페이지 입니다.</h>'.encode('utf-8'))
        elif result.path == '/board':
            params = parse_qs(result.query)
            print(params)

            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('<h1>html이 들어있습니다. Hello World</h>'.encode('utf-8'))

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>Hello World</h>'.encode('utf-8'))


http = HTTPServer(('0.0.0.0', port), MyHttpRequestHandler)
print(f'Server Running on Port{port}')
http.serve_forever()









