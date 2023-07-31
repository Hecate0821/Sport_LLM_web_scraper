import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
ua = UserAgent()

def get_ESPN(page_num):
    url = f'https://www.espn.com/soccer/insider/story/_/id/{page_num}'
    time.sleep(0.1)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    art = soup.find('div', class_='article-body')
    if art == None:
        return 'Error'
    else:
        article = art.text
        return article