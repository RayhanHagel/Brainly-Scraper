# Brainly Answer Scraper by @Hageru-Ray

import requests
from bs4 import BeautifulSoup
from googlesearch import search

RESULTS = 1 # How many answers to find

def brainly(target):
    target = f'brainly {target}'
    limiter = 0
    for results in search(target, tld="com", num=10, stop=10, pause=2):
        if results.find('brainly') != -1:
            limiter += 1
            page = requests.get(results)
            soup = BeautifulSoup(page.content, 'html.parser')
            data = soup.find('div', attrs={'class': 'brn-qpage-next-answer-box-content__section'})
            data = data.text.strip()
            print(data)
            if limiter == RESULTS:
                break
        else:
            pass

# Hageru-Ray

brainly('Who found the American Continent')
