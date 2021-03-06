from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
import RequestHandlerSelector


class ServerClass(BaseHTTPRequestHandler):

    def Start_Respond(self, code, body):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin','*')
        self.send_header('Content-Length', len(body))
        self.send_header('X-Developer', 'Yuqing Zhao')
        self.end_headers()
        self.wfile.write(bytes(body, 'utf-8'))

    def Start_Error(self, err):
        self.send_response(500)
        self.send_header('Content-Type', 'application/json')
        fullError = '{"error":"'+err+'"}'
        self.send_header('Content-Length', len(fullError))
        self.end_headers()
        self.wfile.write(bytes(fullError, 'utf-8'))

    def GetPath(self):
        o = urlparse(self.path)
        return o[2][1:]

    def GetRequestBody(self):
        cLen = self.headers.get('Content-Length')
        if cLen is not None:
            intCLen = int(cLen)
            bd = self.rfile.read(intCLen)
            return bd
        else:
            return None

    def GetCookie(self):
        return self.headers.get('Cookie')

    def Execute(self, method):
        try:
            handler = RequestHandlerSelector.CreateRequestHandler(self.GetPath(), method, self.GetRequestBody(), self.GetCookie())
            if handler is None:
                raise Exception('None request handler')
            result = handler.Execute()
            if result.Code == 200:
                self.Start_Respond(result.Code, result.Body)
            else:
                self.Start_Error(result.Body)
        except Exception as e:
            if len(e.args) > 1:
                self.Start_Error(e.args[1])
            else:
                self.Start_Error(e.args[0])


    def do_GET(self):
        self.Execute('GET')

    def do_POST(self):
        self.Execute('POST')

    # def do_OPTIONS(self):
    #     self.send_response(200)
    #     self.send_header('Access-Control-Allow-Methods', 'GET,PUT,POST')
    #     self.send_header('Access-Control-Allow-Origin', '*')
    #     self.send_header('Access-Control-Allow-Headers', 'X-Cookie')
    #     self.send_header('Access-Control-Allow-Credentials','true')
    #     self.end_headers()
        
