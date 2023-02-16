from bs4 import BeautifulSoup
import urllib.request , urllib.parse, urllib.error
import ssl

#to ignore SSL certified error
cntxt = ssl.create_default_context()
cntxt.check_hostname = False
cntxt.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context = cntxt).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    url = tag.get('href',None)
    print(url)
