from wtvframework import parsehttp, Minisrv, Service

def testparse():
    inp = """GET wtv-1800:/preregister
wtv-ssid: amogus
sus: yes
\r
data
data
data"""

    print(f"in(repr): {repr(inp)}")
    print(f"out: {parsehttp(inp)}")

print("testing parsehttp()")
testparse()

print("starting server")
m = Minisrv()
svc = Service()

xd_data = """
<h1>amogus</h1>
"""

@svc.addhandl("xd")
def b(data):
    return """200 OK
Content-Type: text/html
Content-Length: {len}
\n
{data}
""".format(len=len(xd_data), data=xd_data)

@svc.addhandl("preregister")
def a(data):
    return """200 OK
Connection: Keep-Alive
wtv-initial-key: BCK9Zzas8So=
Content-Type: text/html
wtv-client-time-zone: GMT -0000
wtv-client-time-dst-rule: GMT
wtv-client-date: Fri, 28 Apr 2023 19:12:37 GMT
Content-length: 0
wtv-visit: wtv-1800:/xd
wtv-service: reset
wtv-service: name=wtv-1800 host=127.0.0.1 port=1615 flags=0x00000001 connections=1
\n"""
m.addservice(svc)
m.runserv()