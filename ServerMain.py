from http.server import HTTPServer, BaseHTTPRequestHandler
from ServerClass import ServerClass

httpd = HTTPServer(('', 8000), ServerClass)
print('Im ON')
httpd.serve_forever()
