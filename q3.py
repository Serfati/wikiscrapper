import re
import requests
import pandas as pd

from bs4 import BeautifulSoup
from urllib.request import urlopen
import matplotlib.pyplot as plt


wiki_gal = 'https://en.wikipedia.org/wiki/Gal_Gadot'
wiki = 'https://en.wikipedia.org'
page = urlopen(wiki_gal)
soup = BeautifulSoup(page, 'html.parser')
films_table = soup.find('table', class_='wikitable sortable')
films_urls = [wiki+row.find(href=True)['href']
              for row in films_table.findAll('tr') if row.find_all('td')]
actors_table = []
headers = ['Name', 'Year of Birth', 'Country of Birth', 'No. of Awards']
for url in films_urls:
    film_actors = []
    soup = BeautifulSoup(urlopen(url), features='html.parser')
    raw = (soup.find(id=re.compile(
        ".*cast.*", re.IGNORECASE)).parent).find_next('ul')
    film_actors.extend([[i.find('a').text, wiki+i.find(href=True)['href']]
                        for i in raw.select("li") if i.find('a') and i.find('a').text != 'Gal Gadot'])
    actors_table.extend(film_actors)

#################### only add this for question 3#############################
df = pd.DataFrame(data=actors_table, columns=['name','url'])
# visualization
sns.set()
plt.figure(figsize=(16, 9))
dfh = df.groupby('name').count()
sns.displot(dfh["url"], label="Count")
plt.title("No. of films with Gal Gadot")  # for histogram title
plt.legend()  # for label
plt.show()
#################### only add this for question 3#############################


