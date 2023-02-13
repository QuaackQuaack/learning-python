#binary file mtlb file expect txt like video,img
import urllib.request, urllib.error, urllib.parse

image = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('okthisisname.jpg','wb')
fhand.write(image)
fhand.close()

# here image got binary data from site like in previous code
# then fhand open a binary file for writin only 
# then .write helps to write all recv binary data
# then close 


