import ssl
from bs4 import BeautifulSoup
#import requests
from urllib.request import Request, urlopen

#note some site block the urllib library to protect from bot/spider so 
# we use known browser agent like mozilla , chrome and so on. 
# in this code too we need that so here is alterntive for that
req = Request(
     url= 'https://www.scrapethissite.com/pages/simple/',
     headers = {'User-Agent': 'Mozilla/5.0'}
     )

html = urlopen(req).read()
soup = BeautifulSoup(html,'html.parser')
all = soup('h3')

for tag in all:
    print(tag.text.strip())
    


