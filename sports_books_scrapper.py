from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
from fake_useragent import UserAgent
import string

# path = "C:\Program Files (x86)\chromedriver.exe"

# options = webdriver.ChromeOptions()
# options.add_argument("--headless")

# driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
# https://libgen.rs/search.php?&req=NBA&phrase=1&view=simple&column=def&sort=def&sortmode=ASC&page=1

# Major Sports Leagues:
# NBA, NFL, NHL, MLB, MLS, F1, Premier League, La Liga, League 1……
# Factual information about sports league/organizations is necessary


keywords = ["La Liga", "NBA", "NFL", "NHL", "MLB", "MLS", "F1", "Premier League", "League 1"]


url_left = "https://libgen.rs/search.php?&req="
url_right = "&phrase=1&view=simple&column=def&sort=def&sortmode=ASC&page="

total_file = 0
for keyword in keywords:
    file_count = 0
    ua = UserAgent()
    random_ua = ua.random
    headers = {'User-Agent': random_ua}
    
    pages = 10000
    for page in range(1, 10000):
        keyword = keyword.replace(" ", "%20")
        url = url_left + keyword + url_right + str(page)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', attrs={"title": "Libgen & IPFS & Tor"})
        if links == []:
            break
        for link in links:
            href_value = link.get("href")
            # Check if the href_value is not None and not an empty string
            if href_value and href_value.strip():
                book = requests.get(href_value)
                soup1 = BeautifulSoup(book.text, 'html.parser')
                download_link = soup1.find('a')
                file_name = soup1.find('h1').get_text()
                file_name = file_name.translate(str.maketrans('', '', string.punctuation))
                href = download_link.get("href")
                if href and href.strip():
                    file_count += 1
                file = requests.get(href)
                extension = file.url[href.rfind('/')+1: ]
                extension = extension[extension.rfind('.'):]
                file_name += extension
                with open(file_name, 'wb') as f:
                    for chunk in file.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                file_count += 1
            else:
                print("Link has no value.")
    total_file += file_count
    print(keyword, ": ", file_count, " downloaded")
    time.sleep(2)

print("program end: ", total_file, " downloaded")


