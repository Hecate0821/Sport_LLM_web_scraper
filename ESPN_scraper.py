import requests
from bs4 import BeautifulSoup
import time
import os
from threading import Thread
from fake_useragent import UserAgent
import argparse

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
thread_num = int(500)

# least
least_size = int(100)

login_url = 'https://registerdisney.go.com/jgc/v8/client/ESPN-ONESITE.WEB-PROD/guest/login?langPref=en-US&feature=no-password-reuse'

data = {
  "loginValue": "dicksiekeylen1226@zohomail.com",
  "password": "Xintiao1401"
}


skip_code = {
    '404',
}

# code to retry
retry_code = {
    '403',
}



# please return '404' or 'error' for unwanted pages
def get_content(page_num):
    my_url = url + str(page_num)
    '''
    ua = UserAgent()
    random_ua = ua.random
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHT'}
    response = requests.get(my_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    response_code = response.status_code

    if any(word if int(word) == response_code else False for word in skip_code):
        return 'error: ' + str(skip_code)

    elif any(word if int(word) == response_code else False for word in retry_code):
        my_response_code = ''
        while True:
            time.sleep(5)
            my_response_code = requests.get(my_url, headers=headers)
            if any(word if int(word) == my_response_code else False for word in retry_code):
                pass
            elif any(word if int(word) == response_code else False for word in skip_code):
                    return 'error: ' + str(skip_code)
            else:
                break

    
    while True:
        if 'ESPN Page error' in soup.text:
            return 'error: ESPN page error'
          
        if '403 ERROR' in soup.text:
            time.sleep(10)
            response = requests.get(my_url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')

        else:
            break
    
    art = soup.find('div', class_='article-body')
    if art == None:
        none_massage = 'error: this page:' + my_url + ' has art == none\n'
        return none_massage + soup.text
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
    if '404' in file_content:
        error_404_path = 'error_404_txt/'
        f = open(local_path + error_404_path + file_name + '.txt', 'w', encoding='UTF-8')
        f.write(file_content)
        pass

    elif 'error:' in file_content:
        error_path = 'error_txt/'
        f = open(local_path + error_path + file_name + '.txt', 'w', encoding='UTF-8')
        f.write(file_content)
        pass

    else:
        # encode is needed on windows
        if len(file_content) < least_size:
            size_path = 'sizeunder' + str(least_size) + '/'
            f = open(local_path + size_path + file_name + '.txt', 'w', encoding='UTF-8')
            f.write(file_content)
        f = open(local_path + file_name + '.txt', 'w', encoding='UTF-8')
        f.write(file_content)
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

    #set thread
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
    
    error_404_path = 'error_404_txt/'
    if not os.path.exists(local_path + error_404_path):
                os.mkdir(local_path + error_404_path)

    size_path = 'sizeunder' + str(least_size) + '/'
    if not os.path.exists(local_path + size_path):
                os.mkdir(local_path + size_path)
      
    if args.p:
        check_progress()

    else:

      print('entering main')
      main()
