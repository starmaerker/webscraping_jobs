import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.de/jobs/suche/?q=scala&where=Berlin'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='SearchResults')

jobs = results.find_all('section', class_='card-content')

data_jobs = results.find_all('h2', string=lambda text: 'data' in text.lower())

for job in jobs:
    if job.find('div', id='bad1'):
        continue
    title_elem = job.find('h2', class_='title')
    company_elem = job.find('div', class_='company')
    location_elem = job.find('div', class_='location')
    link = job.find('a')['href']

    if None in (title_elem, company_elem, location_elem):
        continue

    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(link)
    print()





