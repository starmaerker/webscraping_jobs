import requests, time, datetime
from bs4 import BeautifulSoup

URL = 'https://www.lidl.de/de/florabest-liegestuhl-aluminium-mit-armlehne-grau/p332411'
page = requests.get(URL)

while True:
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='add-to-cart')

    print(datetime.datetime.now())

    if soup.find_all('button', {'disabled': ''}):
        print("Artikel noch nicht freigeschaltet.")
    else:
        print("Artikel ist freigeschaltet.")

    time.sleep(1800)


