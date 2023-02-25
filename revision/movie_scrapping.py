from bs4 import BeautifulSoup
from urllib.request import urlopen , Request

movie = list()
i = 1
for page_count in range(1,1118):
    req = Request(
            url=f"https://bflix.gg/movie?page={page_count}",
            headers = {'User-Agent':'Mozilla/5.0'}
            )
    html = urlopen(req).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup.find_all('h2',{"class":"film-name"})
    for tag in tags:
        name = tag.find('a')
        data = name.get('title')
        print(f'We are in page {page_count} : {i} > {data}')
        i += 1
