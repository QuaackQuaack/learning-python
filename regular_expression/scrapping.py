import ssl #suru ma ssl handle 
import re # regular expression 
import urllib.parse, urllib.request, urllib.error

#To ignore the SSL error
cntxt = ssl.create_default_context() 
cntxt.check_hostname = False
cntxt.verify_mode = ssl.CERT_NONE

url = input('enter - ')
html = urllib.request.urlopen(url,context = cntxt).read()
links = re.findall(b'href="(http[s]?://.*?)"',html)
for link in links:
    print(link.decode())
