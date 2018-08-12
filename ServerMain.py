from http.server import HTTPServer
from ServerClass import ServerClass

httpd = HTTPServer(('', 8000), ServerClass)
print('Im ON')
httpd.serve_forever()
