import socket
socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'data.pr4e.org'
port = 80
socks.connect((host,port))
socks.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b''

while True:
    data = socks.recv(5120)
    if len(data) < 1 :break
    count = count + len(data)
    print(len(data),count)
    picture = picture + data

socks.close()
#yesma chai end of header find garni ho kyo hana 
pos = picture.find(b'\r\n\r\n')
print('HEADER LENGTH',pos)
print(picture[:pos].decode())

#yo wala part ma chai image lai save garni ho kyo syd
picture = picture[pos+4:]
fhand = open('filename.jpg','wb')
fhand.write(picture)
fhand.close()



