#in this we gonna learn about urllib library
#as we have done in previous code i.e image_retrieve
#this one is tesko alternative

import urllib.request
urlhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in urlhand:
    print(line.decode().strip())
    

