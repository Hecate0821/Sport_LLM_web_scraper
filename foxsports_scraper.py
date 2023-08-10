import requests
from bs4 import BeautifulSoup
import time
import os
from threading import Thread
from fake_useragent import UserAgent
import argparse
import joblib
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


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

skip_code = {
    '404',
}

# 重试策略
retry_strategy = Retry(
    total=10,  # 最大重试次数
    status_forcelist=[403],  # 需要重试的HTTP状态码
    backoff_factor=10,  # 重试之间的时间间隔因子
    method_whitelist=["GET"]  # 仅对GET请求进行重试
)

class Article:
    content = 'default content'
    type = 'default type'

    def __init__(self):
        self.content = 'default content'
        self.type = 'default_type'

    def set_content(self, content):
        self.content = content

    def set_type(self, type):
        self.type = type


# put your code here
def get_content(page_num):
    article = Article()

    my_url = article_link_list[page_num]
    ua = UserAgent()
    random_ua = ua.random
    headers = {'User-Agent': random_ua}

    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        response = session.get(my_url, headers=headers)

    except:
        article.set_content('max retries in' + my_url)
        article.set_type('max_retries_error')
        return article

    response_code = response.status_code

    if any(word if int(word) == response_code else False for word in skip_code):
        article.set_content(str(skip_code) + 'error in ' + my_url)
        article.set_type(str(skip_code) + 'error')
        return article

    content = BeautifulSoup(response.text, 'html.parser')
    content_txt = content.text

    art = content.find_all('p', class_="mg-t-b-20 ff-h fs-16 lh-1pt88 mg-t-b-20 article-content")
    story = ''

    if art is None:
        article.set_content('response code is :\n' + response_code + '\n + content is :\n' + content_txt)
        article.set_type('art==None_error')
        return article
        
    else:
        for word in art:
            story = story + word.text

        if story != None or story != '' or story != 'null':
            article.set_content('response code is :\n' + str(response_code) + '\n + content is :\n' + story)
            article.set_type('success')
            return article

        else:
            article.set_content(content_txt)
            article.set_type('story==None_error')
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
    if file_content.type == 'success':
        # if file's size under ...
        if len(file_content.content) < least_size:
            f = open(local_path + least_path + file_name + '.txt', 'w', encoding='UTF-8')
            f.write(file_content.content)
            f.close()

        f = open(local_path + file_name + '.txt', 'w', encoding='UTF-8')
        f.write(file_content.content)
        f.close()

    else:
        if len(file_content.content) < least_size:
            type_log_path = local_path + error_path + file_content.type + '.txt'
            f = open(type_log_path, 'a')
            f.write(file_content.content + '\n')


        else:
            # create a directory for each type of error
            type_path = local_path + error_path + file_content.type + '/'
            if not os.path.exists(type_path):
                os.mkdir(type_path)

            f = open(type_path + file_name + '.txt', 'w', encoding='UTF-8')
            f.write(file_content.content)
            f.close()


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
