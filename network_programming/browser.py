import socket
socks = socket.socket()
socks.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
socks.send(cmd)

while True:
    data = socks.recv(512)
    if len(data) <1 :
        break
    print(data.decode(),end='')

socks.close()

