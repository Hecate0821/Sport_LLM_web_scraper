import requests
from bs4 import BeautifulSoup
import time
import os
from threading import Thread
from fake_useragent import UserAgent
import argparse
import joblib

ap_sports_link = joblib.load('./ap_sports_link')
# save directory
const_local_path = './apsports_generalsports/'

# scrape span
start_page = int(0)
end_page = int(0)

# save name
txt_name = 'apSports_'

# thread number
# (end - start) is preferably a multiple of thread number
thread_num = int(100)

# file least size
least_size = int(100)

# error massage list, if in content.text, file would be put in error directory
error_massage = {
    '403',
    '404',
    'error',
    'Error',
}

  
# put your code here
def get_content(page_num):
    url = ap_sports_link[page_num]
    ua = UserAgent()
    random_ua = ua.random
    headers = {'User-Agent': random_ua}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    content_text = soup.text
    
    if any(word if word in content_text else False for word in error_massage):
        error_page = url
        return 'page: ' + error_page + '\nlength: ' + str(len(content_text)) + '\n' + content_text

    while True:
        if 'Too Many Requests' in soup.text:
            time.sleep(10)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
    
        else:
            break
    

    try:
        art = soup.find('div',class_="Page-content")

    except:
        return 'error'

    if art is None:
        return 'error'
    else:
        lines = art.text.strip().split('\n')
        lines = [line for line in lines if line.strip() != '' and 'Flipboard' not in line and 'Published' not in line and 'Copy' not in line and 'Link copied' not in line and 'Reddit' not in line and 'Share' not in line and 'Other news' not in line and 'Pinterest' not in line and 'Print' not in line]
        paragraph = '\n'.join(lines)
        if 'window._taboola' in paragraph:
            paragraph = paragraph.split('window._taboola')[0]
            if '___' in paragraph:
                paragraph = paragraph.split('___')[0]
                return paragraph
            else:
                return paragraph
        else:
            return paragraph


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
    if not any(word if word in file_content else False for word in error_massage):
        # encode is needed on windows
        if len(file_content) < least_size:
            f = open(local_path + least_path + file_name + '.txt', 'w', encoding='UTF-8')
            f.write(file_content)
            f.close()
        f = open(local_path + file_name + '.txt', 'w', encoding='UTF-8')
        f.write(file_content)
        f.close()

    else:
        f = open(local_path + error_path + file_name + '.txt', 'w', encoding='UTF-8')
        f.write(file_content)
        f.close()
        pass


def check_progress():
    workload = int((end_page - start_page) / thread_num)

    for i in range(1, thread_num + 1):
        log_path = local_path + 'log/'

        filename = log_path + 'log_' + str(start_page + (i - 1) * workload) + '_' + str(
            start_page + i * workload) + '.txt'

        f = open(filename, 'r')

        now = int(f.readline().rstrip())

        percentage = (int(now) - start_page - (i - 1) * workload) / workload * 100

        print('Thread ' + str(i) + ': ' + str(now) + ' / ' + str(start_page + i * workload) + ' Progress: ' + str(
            percentage) + '%')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-p", default=False, help='display progress', action="store_true")

    parser.add_argument("start_page", default=-1, help='set start page', type=int)

    parser.add_argument("end_page", default=-1, help='set end page', type=int)

    parser.add_argument("-t", default=-1, help='set threads number', type=int)

    parser.add_argument("-s", default=-1, help='set least size number', type=int)
    
    
    args = parser.parse_args()

    start_page = args.start_page
    end_page = args.end_page

    if args.t != -1:
        thread_num = args.t

    if args.s != -1:
        least_size = args.s

    if not os.path.exists(const_local_path):
        os.mkdir(const_local_path)
    
    local_path = const_local_path + str(start_page) + '_to_' + str(end_page) + '/'
    if not os.path.exists(local_path):
        os.mkdir(local_path)

    log_path = local_path + 'log/'
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    least_path = 'sizeunder' + str(least_size) + '/'
    if not os.path.exists(local_path + least_path):
                os.mkdir(local_path + least_path)

    error_path = 'error_txt/'
    if not os.path.exists(local_path + error_path):
                os.mkdir(local_path + error_path)

    if args.p:
        check_progress()

    else:
        main()




