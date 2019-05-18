import sys
import socket

import ntplib

correction = int(open('config.txt').read())

client = ntplib.NTPClient()
time = client.request('ntp2.stratum2.ru').tx_time
#print(time.tx_time)
new_time = time + correction
print(new_time)

sys.exit()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 123))
server.listen(10)
while True:
    cl, das = server.accept()
    cl.sendall(str(time).encode())
    cl.close()
'''
while True:
    msg = cl.recv(1024)
    print(msg)
    if msg:
        cl.sendall(str(now).encode())
        cl.close()'''
