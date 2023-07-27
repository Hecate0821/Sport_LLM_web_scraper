import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
from fake_useragent import UserAgent

def get_asap_interview(page_num):
    url = f'https://www.asapsports.com/show_interview.php?id={page_num}'
    time.sleep(0.1)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        art = soup.find(style="padding: 10px;")
        article = art.text
        return article
    except:
        return 'error'



