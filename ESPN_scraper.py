import requests
from bs4 import BeautifulSoup
import time
import os
from threading import Thread
from fake_useragent import UserAgent

# article site url
url = 'https://www.espn.com/soccer/insider/story/_/id/'

# save directory
const_local_path = './espnArticles/'

# save_name
txt_name = 'espn_'

# scrape span
start_page = int(500)
end_page = int(38200500)

# thread number
# (end - start) is preferably a multiple of thread number
thread_num = int(1000)

login_url = 'https://registerdisney.go.com/jgc/v8/client/ESPN-ONESITE.WEB-PROD/guest/login?langPref=en-US&feature=no-password-reuse'

data = {
  "loginValue": "dicksiekeylen1226@zohomail.com",
  "password": "Xintiao1401"
}



# please return '404' or 'error' for unwanted pages
def get_content(page_num):
    my_url = url + str(page_num)
    response = sess.get(my_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    art = soup.find('div', class_='article-body')
    if art == None:
        return 'Error'
    else:
        article = art.text
        return article


def save_log(start, end, now):
    filename = log_path + 'log_' + str(start) + '_' + str(end) + '.txt'
    f = open(filename, 'w', encoding='UTF-8')
    f.write(str(now))


def check_log(start, end):
    filename = log_path + 'log_' + str(start) + '_' + str(end) + '.txt'
    if not os.path.exists(filename):
        f = open(filename, 'w')

    f = open(filename, 'r')
    try:
        scraped = int(f.readline().rstrip())

        return scraped

    except:
        return start


def main():
    workload = int((end_page - start_page) / thread_num)

    thread_list = []

    for i in range(1, thread_num+1):
        t = Thread(target=scraper, args=[start_page + (i-1) * workload, start_page + i * workload, ])
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    return 0


def scraper(start, end):
    now = 0
    while True:
        if now < check_log(start, end):
            now = check_log(start, end)

        if now > end:
            break

        content = get_content(now)
        save_as_txt(txt_name + str(now), content)
        save_log(start, end, now)
        now = now + 1


def save_as_txt(file_name, file_content):
    if (file_content[0:5] != 'Error') and (file_content[0:5] != 'error') and (file_content[0:3] != '404'):
        # encode is needed on windows
        f = open(local_path + file_name + '.txt', 'w', encoding='UTF-8')
        f.write(file_content)
        f.close()

    else:
        pass


if __name__ == '__main__':
    local_path = const_local_path + str(start_page) + '_to_' + str(end_page) + '/'

    if not os.path.exists(local_path):
        os.mkdir(local_path)

    log_path = local_path + 'log/'

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    rst = 1

    ua = UserAgent()
    random_ua = ua.random
    header = {'User-Agent': random_ua}
    sess = requests.session()

    sess.post(login_url, data=data, headers=header)

    while True:
        my_count = 0
        print('in round:' + str(my_count))
        my_count = my_count + 1
        try:
            rst = main()
            if rst == 0:
                break

        except KeyboardInterrupt:
            print('exit')
            time.sleep(3)
            break

        except:
            print("restarting...")
            time.sleep(3)
            pass
