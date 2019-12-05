import machine
import network
import esp32
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('kitchencath', '')
wlan.ifconfig()

html = """
    <!DOCTYPE html><html>
    <head>
        <title>ESP32 MicroPython</title>
    </head><body>
        <h1>ESP32 MicroPython</h1>
        <table border="1"> <tr><th>Temp(C)</th><th>Hall()</th></tr> %s </table>
    </body></html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    #rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    #response = html % '\n'.join(rows)
    rows=['<tr><td> %s </td><td> %s </td></tr>'%( 
            (esp32.raw_temperature() - 32) * 5.0/9.0,
            esp32.hall_sensor() 
        )]
    response = html % '\n'.join(rows)
    cl.send(response)
    cl.close()