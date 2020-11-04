from bs4 import BeautifulSoup
import mwparserfromhell
import json
import pandas as pd
import re
from urllib.request import urlopen
from urllib.parse import urlencode

API_URL = "https://en.wikipedia.org/w/api.php"
wiki_gal = 'https://en.wikipedia.org/wiki/Gal_Gadot'
wiki = 'https://en.wikipedia.org'


def parse(title):
    data = {"action": "query", "prop": "revisions", "rvprop": "content",
            "rvslots": "main", "rvlimit": 1, "titles": title,
            "format": "json", "formatversion": "2"}
    raw = urlopen(API_URL, urlencode(data).encode()).read()
    res = json.loads(raw)
    revision = res["query"]["pages"][0]["revisions"][0]
    text = revision["slots"]["main"]["content"]
    return mwparserfromhell.parse(text)

def find_number_of_awards(page_actor):
    page = urlopen(page_actor)
    page_actor = BeautifulSoup(page, 'html.parser')
    awards1 = awards2 = awards3 = -1
    try:
        awards1 = len(
            page_actor.find('span', {'id': 'Awards_and_nominations'}).findNext('table').find_all('td', {
                'class': 'yes table-yes2'}))
    except:
        pass
    try:
        awards2 = len(page_actor.find('span', {'id': 'Awards_and_nominations'}).findNext('table').findNext('table').find_all('td', {
            'class': 'yes table-yes2'}))
    except:
        pass
    try:
        url = page_actor.find('a', {'title': re.compile(
            'List of awards and nominations received by')})['href']
        page_awards = BeautifulSoup(
            urlopen("https://en.wikipedia.org/" + url), "lxml")
        awards3 = len(page_awards.findAll(
            'td', {'class': 'yes table-yes2'}, text=re.compile("Won")))
    except:
        pass
    if awards1 != -1 or awards2 != -1 or awards3 != -1:
        return max(awards1, awards2, awards3)
    return 0

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

    if len(actors_table) > 5:
        break

for i, v in enumerate(actors_table):
    name, url = v
    info_box = ''
    try:
        wiki = parse(name)
        info_box = wiki.filter_templates(matches="Infobox person")[0]
        v.append(int(info_box.get(
            'birth_date').value.filter_templates()[0].get(1)))
    except:
        v.append(0)
    try:
        country_raw = info_box.get('birth_place').value
        j = country_raw.rfind(']')
        d = ",!?/&-:;@'<>{}"
        country_raw = re.split("["+"\\".join(d)+"]", country_raw[j+2:])
        country_raw = [
            'U.S.', country_raw[0].strip()][country_raw[0].strip() != '']
        v.append(country_raw)
    except:
        v.append(0)
    v.append(0)
df = pd.DataFrame(data=actors_table)
pd.set_option('display.max_columns', 5)
print(df)  # answer for q1

