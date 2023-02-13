# in this progam we will learn about retriving data in block

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('okbaby.jpg','wb')
size = 0 
while True:
    info = img.read(100000)
    if len(info) < 1 : break
    size = size + len(info)
    fhand.write(info)

print(size,'character copied')
fhand.close()
