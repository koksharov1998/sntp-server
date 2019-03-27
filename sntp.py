import datetime
import socket

now = datetime.datetime.now()
print(now)

correction = int(open('config.txt').read())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 123))
server.listen(10)
cl, das = server.accept()
cl.sendall(str(now).encode())
cl.close()
'''
while True:
    msg = cl.recv(1024)
    print(msg)
    if msg:
        cl.sendall(str(now).encode())
        cl.close()'''
