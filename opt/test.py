import requests
from bs4 import BeautifulSoup

res = requests.get('https://kamoy4.com/')

soup = BeautifulSoup(res.text, 'html.parser')

title_text = soup.find('title').get_text()
print(title_text)
