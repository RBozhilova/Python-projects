import requests as re
from bs4 import BeautifulSoup

r = re.get('https://novini.bg/')

html_soup = BeautifulSoup(r.content, 'html.parser')

articles = html_soup.find_all('title')
print(articles)