import requests as re
from bs4 import BeautifulSoup
import csv
import pandas as pd
r = re.get('https://offnews.bg/')
r.encoding = r.apparent_encoding

html_soup = BeautifulSoup(r.content, 'html.parser')

articles = html_soup.find_all('a')


article_titles = set()

for article in articles:
    article_title = article.get('title')

    if not article_title is None and len(article_title) >= 10:
         article_titles.add(article.get('title'))


for article in article_titles:
    print(article)

df =  pd.DataFrame(article_titles)
df.to_csv('article_titles.csv', encoding="utf-8")