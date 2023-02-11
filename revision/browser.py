import socket
socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socks.connect(('py4e.com',443))
cmd = 'GET https://www.py4e.com/html3/12-network HTTP/1.0/r/n/r/n'.encode()
socks.send(cmd)
while True:
    data = socks.recv(512)
    if len(data)<0:
        break
    print(data.decode(),end='')

socks.close()
