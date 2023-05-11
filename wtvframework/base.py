from . import parsehttp
from socket import AF_INET, SOCK_STREAM, socket

class Service:
    def __init__(self, service: str="wtv-1800"):
        self.name = service
        self.handlers = {}
    def addhandl(self, name):
        def addh(handler):
            self.handlers[name] = handler
        return addh

class Minisrv:
    def __init__(self, name: str="server"):
        self.name = name
        self.services: list[Service] = []
    def addservice(self, srv: Service):
        self.services.append(srv)
    def handle(self, data: bytes):
        data: dict[str, str] = parsehttp(data.decode())
        service = data['url'].split(":",1)[0]
        handl = data['url'].split(":/",1)[1]
        for i in self.services:
            print(i.name)
            if i.name == service:
                for a in i.handlers:
                    print(a)
                    print(handl)
                    if a == handl:
                        outdata: str = i.handlers[a](data)
                        if type(outdata) == type(""): outdata = outdata.encode()
                        return outdata
        return f"400 WTVFramework ran into problem, error: URL {data['url']} not found\r\nContent-length: 0\r\nContent-Type: text/html\r\nwtv-service: reset\r\n".encode()
    def runserv(self, host: str='localhost', port: int=1615, maxlisten: int=15):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(maxlisten)
        while True:
            sock, addr = self.sock.accept()
            out = self.handle(sock.recv(16384))
            print(out)
            sock.send(out)
            sock.close()