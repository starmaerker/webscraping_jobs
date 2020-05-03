import requests, pprint
from bs4 import BeautifulSoup

URL = 'https://www.monster.de/jobs/suche/?q=python&where=Berlin'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='SearchResults')

jobs = results.find_all('section', class_='card-content')

counter = 1

for job in jobs:
    title_elem = job.find('h2', class_='title')
    company_elem = job.find('div', class_='company')
    location_elem = job.find('div', class_='location')
    print(str(counter) + ': ')
    if title_elem is not None:
        print(title_elem.text)
    if company_elem is not None:
        print(company_elem.text)
    if location_elem is not None:
        print(location_elem.text)
    print()
    counter += 1





