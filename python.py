from  http.server import  BaseHTTPRequestHandler, HTTPServer
hostName="localhost"
serverPort=8080
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.end_headers()
        self.wfile.write(bytes("Hello you have connected to lcoalhost", "utf-8"))
if __name__ == '__main__':
    webServer = HTTPServer((hostName,serverPort),MyServer)
    print("localost started at htpps://%s-%s" % (hostName,serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
