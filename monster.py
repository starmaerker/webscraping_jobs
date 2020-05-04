import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.de/jobs/suche/?q=python&where=Berlin'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='SearchResults')

jobs = results.find_all('section', class_='card-content')

for job in jobs:
    title_elem = job.find('h2', class_='title')
    company_elem = job.find('div', class_='company')
    location_elem = job.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()





