from wtvframework import parsehttp, Minisrv, Service, Responce

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
<a href=\"wtv-brazil:/u-going-to-brazil\">brazil</a>"""

@svc.addhandl("xd")
def b(data):
    return Responce(200, data=xd_data)

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
wtv-service: name=wtv-1800 host=127.0.0.1 port=1615 flags=0x00000002 connections=1
wtv-service: name=wtv-brazil host=127.0.0.1 port=1615 flags=0x00000002
wtv-service: name=NON-WTV-XD host=127.0.0.1 port=1615 flags=0x00000002
\n"""

svc2 = Service("wtv-brazil")

brazil = """
<h1>u going to brazil</h1>
<h1>fun fact: webtv can open any service</h1>
"""

@svc2.addhandl("u-going-to-brazil")
def c(data):
    return Responce(400, err_data="U GOING TO BRASIL NOW")

svc3 = Service("NON-WTV-XD".lower())
data2 = """
<h1>non wtv service xd</h1>"""
@svc3.addhandl("")
def nonwtv(data):
    return """200 OK
Content-Type: text/html
Content-Length: {len}
\n
{data}
""".format(len=len(data2), data=data2)

m.addservice(svc)
m.addservice(svc2)
m.addservice(svc3)
m.runserv()

# client:ConfirmConnectSetup?serviceType=custom&machine=127.0.0.1&port=1615&useEncryption=true&connect=Connect