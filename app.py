import requests, pprint
from bs4 import BeautifulSoup

URL = 'https://www.monster.de/jobs/suche/?q=python&where=Berlin'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)

