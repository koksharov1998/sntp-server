import sys
import socket
from time import ctime

import ntplib

s = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
s.sendto(b'\x1b' + 47 * b'\0', ('ntp2.stratum2.ru', 123))
p = ntplib.NTPPacket(s.recv(1024))
print(p)

print(ctime(p.recv_timestamp))


sys.exit()
correction = int(open('config.txt').read())
print(correction)

client = ntplib.NTPClient()
response = client.request('ntp2.stratum2.ru')
print(ctime(response.tx_time))
new_time = response.tx_time + correction
print(new_time)
print()
print(response.recv_timestamp)
print(ctime(response.recv_timestamp))
print(response.tx_timestamp)
print(ctime(response.tx_timestamp))
response.recv_timestamp += correction
response.tx_timestamp += correction
print(ctime(response.tx_time))


sys.exit()
server = socket.socket()
server.bind(('localhost', 123))
server.listen(10)

connection, address = server.accept()

while True:
    data = connection.recv(1024)
    print(data.decode())
