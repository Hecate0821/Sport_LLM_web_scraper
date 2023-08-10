
import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
ua = UserAgent()
import joblib

url='https://www.cyclingnews.com/sitemap.xml'

def get_sitemap(url):
    sitemap_url = url

    # Get the sitemap
    response = requests.get(sitemap_url)

    # Parse the XML response with BeautifulSoup
    soup = BeautifulSoup(response.content, 'xml')
    urls = soup.find_all('loc')
    sitemap_url_list = []
    for url in urls:
        url_text = url.get_text()
        sitemap_url_list.append(url_text)
        
    article_link_list = []
    for link in (sitemap_url_list[:236]):
        sitemap_url = link
        ua = UserAgent()
        random_ua = ua.random
        headers = {'User-Agent':random_ua}
        response = requests.get(sitemap_url, headers=headers)

        # Parse the XML response with BeautifulSoup
        soup = BeautifulSoup(response.content, 'xml')
        urls = soup.find_all('loc')
        for url in urls:
            # Extract the URL text
            url_text = url.get_text()
            article_link_list.append(url_text)
    return article_link_list

joblib.dump('cycling_list',get_sitemap(url))
