# in this program I will learn about pulling out various part of each tag

from bs4 import BeautifulSoup
import ssl
import urllib.request, urllib.error, urllib.parse

#managing SSL certified error
cntxt = ssl.create_default_context()
cntxt.check_hostname = False
cntxt.verify_mode = ssl.CERT_NONE

url = input(' Enter url - ')
html = urllib.request.urlopen(url, context = cntxt).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print('tag',tag)
    print('url', tag.get('href',None))
    print('contents:',tag.contents[0]) #content method  is related to bs4 
    print('Attrs:',tag.attrs)
