import requests
from bs4 import BeautifulSoup
url = 'https://www.allsides.com/media-bias/media-bias-ratings'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')
print(rows)
row = rows[0]
name = row.select_one('.source-title').text.strip()
print(name)

