# A simple example of send function
import socket

socks = socket.socket();
socks.connect(('127.0.0.1',9090))
data = 'hello Server!'
socks.send(data.encode())
Fromserver = socks.recv(1024)
print(Fromserver.decode())
