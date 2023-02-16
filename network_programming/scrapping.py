import re
import urllib.request, urllib.parse, urllib.error
import ssl #SSL enforce us to make secure connection i.e HTTPS

#ignore SSl certificate errors
cntx = ssl.create_default_context() #for every connection we need context
cntx.check_hostname = False
cntx.verify_mode = ssl.CERT_NONE #error handling 

#this downside block is for image scrapping 
url =  input('enter - ')
html = urllib.request.urlopen(url, context = cntx).read()
links = re.findall(b'href="(http[s]?://.*?)"',html)
for link in links:
    print(link.decode())



