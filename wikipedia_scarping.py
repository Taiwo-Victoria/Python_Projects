#           Scraping Wikipedia pages

import requests
import string
from bs4 import BeautifulSoup
import warnings

warnings.catch_warnings()
warnings.simplefilter("ignore")

Search = input("Enter your search keyqword: ")
capital = string.capwords(Search)
lists = capital.split()
word = "_".join(lists)

url = "https://en.wikipedia.org/wiki/"+word

def wiki_scrape(url):
    url_open = requests.get(url) # to send http request
    scrape = BeautifulSoup(url_open.content, 'html.parser')
    details = scrape('table', {'class':'infobox'})
    
    for i in details:
        content = i.find_all('tr')
        for j in content:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading is not None and detail is not None:
                for x,y in zip(heading,detail):
                    print("{}   ::  {}".format(x.text, y.text))
                    print("-----------------")
    for i in range(1,3):
        print(scrape('p')[i].text)
wiki_scrape(url)