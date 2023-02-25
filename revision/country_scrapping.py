from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request(
        url = 'https://www.scrapethissite.com/pages/simple/',
        headers = {'User-Agent':'Mozilla/5.0'}
        )
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
all = soup('h3')

for index, tag in enumerate(all):
    print(f'{index}',tag.text.strip())

