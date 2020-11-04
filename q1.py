from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

wiki_prefix = "https://en.wikipedia.org/"
wiki = "https://en.wikipedia.org/wiki/Gal_Gadot"
html = urlopen(wiki)
soup = BeautifulSoup(html, features='html.parser')
films_table = soup.find('table', class_='wikitable sortable').findAll('tr')
headers = films_table[0]
rows = films_table[1:]
headers = [header.get_text().strip() for header in headers.find_all('th')]
table = [[cell.get_text().strip() for cell in row.find_all('td')]
         for row in rows]
for i, v in enumerate(table):
    if not v[0].isdigit() and v[0] != 'TBA':
        table[i].insert(0, table[i-1][0])
df = pd.DataFrame(data=table, columns=headers)
pd.set_option('display.max_columns', 5)
print(df)  # answer for q1
