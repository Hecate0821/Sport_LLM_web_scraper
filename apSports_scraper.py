import requests
from bs4 import BeautifulSoup
import time
import os
from threading import Thread
from fake_useragent import UserAgent
import joblib
import argparse


# article site url

ap_sports_link = joblib.load('./ap_sports_link')
# save directory
const_local_path = './apsports_generalsports/'

# scrape span
start_page = int(0)
end_page = int(1000)

# save name
txt_name = 'apSports_'

# thread number
# (end - start) is preferably a multiple of thread number
thread_num = int(100)


# please return '404' or 'error' for unwanted pages 
def get_apsports(page_num):
    url = ap_sports_link[page_num]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        art = soup.find('div',class_="Page-content")

    except:
        return 'error'

    if art is None:
        print('art is NONE in :' + str(page_num))
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

        content = get_apsports(now)
        save_as_txt(txt_name + str(now), content)
        save_log(start, end, now)
        now = now + 1


def save_as_txt(file_name, file_content):
    if (file_content[0:5] != 'Error') and (file_content[0:5] != 'error') and (file_content[0:3] != '404'):
        if file_content[0:3] == '404':
            print('404!!!!!!!\n\n\n\n')
        # encode is needed on windows
        f = open(local_path + file_name + '.txt', 'w', encoding='UTF-8')
        f.write(file_content)
        f.close()

    else:
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
    local_path = const_local_path + str(start_page) + '_to_' + str(end_page) + '/'

    if not os.path.exists(local_path):
        os.mkdir(local_path)

    log_path = local_path + 'log/'

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    rst = 1

    parser = argparse.ArgumentParser()

    parser.add_argument("--p", default=False, help='display progress', action="store_true")

    args = parser.parse_args()

    if args.p:
        check_progress()

    else:
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
