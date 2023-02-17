from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request(
        url = 'https://www.scrapethissite.com/pages/forms/',
        headers = {'User-Agent': "Mozilla/5.0"}
        )

html = urlopen(req).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup.find_all("td",{"class" : "name"})

for tag in tags:
    print(tag.text.strip())

