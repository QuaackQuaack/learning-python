import urllib.request, urllib.parse, urllib.error

imghandle = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('stuff.jpg','wb')
size  = 0 
while True:
    info = imghandle.read(10000)
    if len(info)< 1: break
    size = size + len(info)
    fhand.write(info)

fhand.close()
