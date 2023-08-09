import requests
from bs4 import BeautifulSoup
import time
import os
from threading import Thread
from fake_useragent import UserAgent
import argparse
import joblib

# article site url

article_link_list = joblib.load('./fox_sports_link')
# save directory
const_local_path = './foxsports_generalsports/'

# scrape span
start_page = int(0)
end_page = int(1232800)

# save name
txt_name = 'foxsports_'

# thread number
# (end - start) is preferably a multiple of thread number
thread_num = int(100)

# file least size
least_size = int(100)

# error massage list, if in content.text, file would be put in error directory
error_massage = {
    'error',
    'Error',
}

# code to skip
skip_code = {
    '404',
}

# code to retry
retry_code = {
    '403',
}

# put your code here
def get_content(page_num):
    my_url = article_link_list[page_num]
    ua = UserAgent()
    random_ua = ua.random
    headers = {'User-Agent': random_ua}
    response = requests.get(my_url, headers=headers)

    response_code = response.status_code

    if any(word if int(word) == response_code else False for word in skip_code):
        return 'error ' + str(skip_code)

    elif any(word if int(word) == response_code else False for word in retry_code):
        my_response_code = ''
        while True:
            time.sleep(5)
            my_response_code = requests.get(my_url, headers=headers)
            if any(word if int(word) == my_response_code else False for word in retry_code):
                pass
            elif any(word if int(word) == response_code else False for word in skip_code):
                    return 'error ' + str(skip_code)
            else:
                break

    content = BeautifulSoup(response.text, 'html.parser')
    content_txt = content.text

    art = content.find_all('p', class_="mg-t-b-20 ff-h fs-16 lh-1pt88 mg-t-b-20 article-content")
    story = ''
    if art == None:
        return 'error: art == None\n' + content_txt
    else:
        for word in art:
            story = story + word.text
        if story != None or story != '' or story != 'null':
            return story
        else:
            return 'error: story == None\n'

    # put your code below:


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

    for i in range(1, thread_num + 1):
        t = Thread(target=scraper, args=[start_page + (i - 1) * workload, start_page + i * workload, ])
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
    # if no error in file content
    if not any(word if word in file_content else False for word in error_massage):

        # if file's size under ...
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

    # cmd
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", default=False, help='display progress', action="store_true")

    parser.add_argument("start_page", default=0, help='set start page', type=int)

    parser.add_argument("end_page", default=0, help='set end page', type=int)

    parser.add_argument("-t", default=100, help='set threads number', type=int)

    parser.add_argument("-s", default=100, help='set least size number', type=int)

    args = parser.parse_args()

    # set page
    start_page = args.start_page
    end_page = args.end_page

    # set thread
    thread_num = args.t

    # set least size
    least_size = args.s

    # create dirs
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
