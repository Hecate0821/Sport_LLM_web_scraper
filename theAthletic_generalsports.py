import requests
from bs4 import BeautifulSoup
import time
import os
from threading import Thread
import numpy

url = 'https://theathletic.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}

const_local_path = '/root/scraper/theAthletic/'

start_page = int(0)
end_page = int(4800000)

local_path = const_local_path + str(start_page) + '_to_' + str(end_page) + '/'


def check_progress():
    workload = int((end_page - start_page) / 100)

    for i in range(1, 101):
        filename = local_path + 'log_' + str(start_page + (i-1) * workload) + '_' + str(start_page + i * workload) + '.txt'

        f = open(filename, 'r')

        now = int(f.readline().rstrip())

        percentage = (int(now) - start_page - (i-1) * workload) / workload * 100

        print('Thread ' + str(i) + ': ' + str(now) + ' / ' + str(start_page + i * workload) + ' Progress: ' + str(percentage) + '%')

    time.sleep(5)

def save_log(start, end, now):
    filename = local_path + 'log_' + str(start) + '_' + str(end) + '.txt'
    f = open(filename, 'w', encoding='UTF-8')
    f.write(str(now))


def check_log(start, end):
    filename = local_path + 'log_' + str(start) + '_' + str(end) + '.txt'
    if not os.path.exists(filename):
        f = open(filename, 'w')

    f = open(filename, 'r')
    try:
        scraped = int(f.readline().rstrip())

        return scraped

    except:
        return start


def main():

    workload = int((end_page - start_page) / 100)

    t1 = Thread(target=scraper, args=[start_page + 0 * workload, start_page + 1 * workload, ])
    t2 = Thread(target=scraper, args=[start_page + 1 * workload, start_page + 2 * workload, ])
    t3 = Thread(target=scraper, args=[start_page + 2 * workload, start_page + 3 * workload, ])
    t4 = Thread(target=scraper, args=[start_page + 3 * workload, start_page + 4 * workload, ])
    t5 = Thread(target=scraper, args=[start_page + 4 * workload, start_page + 5 * workload, ])
    t6 = Thread(target=scraper, args=[start_page + 5 * workload, start_page + 6 * workload, ])
    t7 = Thread(target=scraper, args=[start_page + 6 * workload, start_page + 7 * workload, ])
    t8 = Thread(target=scraper, args=[start_page + 7 * workload, start_page + 8 * workload, ])
    t9 = Thread(target=scraper, args=[start_page + 8 * workload, start_page + 9 * workload, ])
    t10 = Thread(target=scraper, args=[start_page + 9 * workload, start_page + 10 * workload, ])
    t11 = Thread(target=scraper, args=[start_page + 10 * workload, start_page + 11 * workload, ])
    t12 = Thread(target=scraper, args=[start_page + 11 * workload, start_page + 12 * workload, ])
    t13 = Thread(target=scraper, args=[start_page + 12 * workload, start_page + 13 * workload, ])
    t14 = Thread(target=scraper, args=[start_page + 13 * workload, start_page + 14 * workload, ])
    t15 = Thread(target=scraper, args=[start_page + 14 * workload, start_page + 15 * workload, ])
    t16 = Thread(target=scraper, args=[start_page + 15 * workload, start_page + 16 * workload, ])
    t17 = Thread(target=scraper, args=[start_page + 16 * workload, start_page + 17 * workload, ])
    t18 = Thread(target=scraper, args=[start_page + 17 * workload, start_page + 18 * workload, ])
    t19 = Thread(target=scraper, args=[start_page + 18 * workload, start_page + 19 * workload, ])
    t20 = Thread(target=scraper, args=[start_page + 19 * workload, start_page + 20 * workload, ])
    t21 = Thread(target=scraper, args=[start_page + 20 * workload, start_page + 21 * workload, ])
    t22 = Thread(target=scraper, args=[start_page + 21 * workload, start_page + 22 * workload, ])
    t23 = Thread(target=scraper, args=[start_page + 22 * workload, start_page + 23 * workload, ])
    t24 = Thread(target=scraper, args=[start_page + 23 * workload, start_page + 24 * workload, ])
    t25 = Thread(target=scraper, args=[start_page + 24 * workload, start_page + 25 * workload, ])
    t26 = Thread(target=scraper, args=[start_page + 25 * workload, start_page + 26 * workload, ])
    t27 = Thread(target=scraper, args=[start_page + 26 * workload, start_page + 27 * workload, ])
    t28 = Thread(target=scraper, args=[start_page + 27 * workload, start_page + 28 * workload, ])
    t29 = Thread(target=scraper, args=[start_page + 28 * workload, start_page + 29 * workload, ])
    t30 = Thread(target=scraper, args=[start_page + 29 * workload, start_page + 30 * workload, ])
    t31 = Thread(target=scraper, args=[start_page + 30 * workload, start_page + 31 * workload, ])
    t32 = Thread(target=scraper, args=[start_page + 31 * workload, start_page + 32 * workload, ])
    t33 = Thread(target=scraper, args=[start_page + 32 * workload, start_page + 33 * workload, ])
    t34 = Thread(target=scraper, args=[start_page + 33 * workload, start_page + 34 * workload, ])
    t35 = Thread(target=scraper, args=[start_page + 34 * workload, start_page + 35 * workload, ])
    t36 = Thread(target=scraper, args=[start_page + 35 * workload, start_page + 36 * workload, ])
    t37 = Thread(target=scraper, args=[start_page + 36 * workload, start_page + 37 * workload, ])
    t38 = Thread(target=scraper, args=[start_page + 37 * workload, start_page + 38 * workload, ])
    t39 = Thread(target=scraper, args=[start_page + 38 * workload, start_page + 39 * workload, ])
    t40 = Thread(target=scraper, args=[start_page + 39 * workload, start_page + 40 * workload, ])
    t41 = Thread(target=scraper, args=[start_page + 40 * workload, start_page + 41 * workload, ])
    t42 = Thread(target=scraper, args=[start_page + 41 * workload, start_page + 42 * workload, ])
    t43 = Thread(target=scraper, args=[start_page + 42 * workload, start_page + 43 * workload, ])
    t44 = Thread(target=scraper, args=[start_page + 43 * workload, start_page + 44 * workload, ])
    t45 = Thread(target=scraper, args=[start_page + 44 * workload, start_page + 45 * workload, ])
    t46 = Thread(target=scraper, args=[start_page + 45 * workload, start_page + 46 * workload, ])
    t47 = Thread(target=scraper, args=[start_page + 46 * workload, start_page + 47 * workload, ])
    t48 = Thread(target=scraper, args=[start_page + 47 * workload, start_page + 48 * workload, ])
    t49 = Thread(target=scraper, args=[start_page + 48 * workload, start_page + 49 * workload, ])
    t50 = Thread(target=scraper, args=[start_page + 49 * workload, start_page + 50 * workload, ])
    t51 = Thread(target=scraper, args=[start_page + 50 * workload, start_page + 51 * workload, ])
    t52 = Thread(target=scraper, args=[start_page + 51 * workload, start_page + 52 * workload, ])
    t53 = Thread(target=scraper, args=[start_page + 52 * workload, start_page + 53 * workload, ])
    t54 = Thread(target=scraper, args=[start_page + 53 * workload, start_page + 54 * workload, ])
    t55 = Thread(target=scraper, args=[start_page + 54 * workload, start_page + 55 * workload, ])
    t56 = Thread(target=scraper, args=[start_page + 55 * workload, start_page + 56 * workload, ])
    t57 = Thread(target=scraper, args=[start_page + 56 * workload, start_page + 57 * workload, ])
    t58 = Thread(target=scraper, args=[start_page + 57 * workload, start_page + 58 * workload, ])
    t59 = Thread(target=scraper, args=[start_page + 58 * workload, start_page + 59 * workload, ])
    t60 = Thread(target=scraper, args=[start_page + 59 * workload, start_page + 60 * workload, ])
    t61 = Thread(target=scraper, args=[start_page + 60 * workload, start_page + 61 * workload, ])
    t62 = Thread(target=scraper, args=[start_page + 61 * workload, start_page + 62 * workload, ])
    t63 = Thread(target=scraper, args=[start_page + 62 * workload, start_page + 63 * workload, ])
    t64 = Thread(target=scraper, args=[start_page + 63 * workload, start_page + 64 * workload, ])
    t65 = Thread(target=scraper, args=[start_page + 64 * workload, start_page + 65 * workload, ])
    t66 = Thread(target=scraper, args=[start_page + 65 * workload, start_page + 66 * workload, ])
    t67 = Thread(target=scraper, args=[start_page + 66 * workload, start_page + 67 * workload, ])
    t68 = Thread(target=scraper, args=[start_page + 67 * workload, start_page + 68 * workload, ])
    t69 = Thread(target=scraper, args=[start_page + 68 * workload, start_page + 69 * workload, ])
    t70 = Thread(target=scraper, args=[start_page + 69 * workload, start_page + 70 * workload, ])
    t71 = Thread(target=scraper, args=[start_page + 70 * workload, start_page + 71 * workload, ])
    t72 = Thread(target=scraper, args=[start_page + 71 * workload, start_page + 72 * workload, ])
    t73 = Thread(target=scraper, args=[start_page + 72 * workload, start_page + 73 * workload, ])
    t74 = Thread(target=scraper, args=[start_page + 73 * workload, start_page + 74 * workload, ])
    t75 = Thread(target=scraper, args=[start_page + 74 * workload, start_page + 75 * workload, ])
    t76 = Thread(target=scraper, args=[start_page + 75 * workload, start_page + 76 * workload, ])
    t77 = Thread(target=scraper, args=[start_page + 76 * workload, start_page + 77 * workload, ])
    t78 = Thread(target=scraper, args=[start_page + 77 * workload, start_page + 78 * workload, ])
    t79 = Thread(target=scraper, args=[start_page + 78 * workload, start_page + 79 * workload, ])
    t80 = Thread(target=scraper, args=[start_page + 79 * workload, start_page + 80 * workload, ])
    t81 = Thread(target=scraper, args=[start_page + 80 * workload, start_page + 81 * workload, ])
    t82 = Thread(target=scraper, args=[start_page + 81 * workload, start_page + 82 * workload, ])
    t83 = Thread(target=scraper, args=[start_page + 82 * workload, start_page + 83 * workload, ])
    t84 = Thread(target=scraper, args=[start_page + 83 * workload, start_page + 84 * workload, ])
    t85 = Thread(target=scraper, args=[start_page + 84 * workload, start_page + 85 * workload, ])
    t86 = Thread(target=scraper, args=[start_page + 85 * workload, start_page + 86 * workload, ])
    t87 = Thread(target=scraper, args=[start_page + 86 * workload, start_page + 87 * workload, ])
    t88 = Thread(target=scraper, args=[start_page + 87 * workload, start_page + 88 * workload, ])
    t89 = Thread(target=scraper, args=[start_page + 88 * workload, start_page + 89 * workload, ])
    t90 = Thread(target=scraper, args=[start_page + 89 * workload, start_page + 90 * workload, ])
    t91 = Thread(target=scraper, args=[start_page + 90 * workload, start_page + 91 * workload, ])
    t92 = Thread(target=scraper, args=[start_page + 91 * workload, start_page + 92 * workload, ])
    t93 = Thread(target=scraper, args=[start_page + 92 * workload, start_page + 93 * workload, ])
    t94 = Thread(target=scraper, args=[start_page + 93 * workload, start_page + 94 * workload, ])
    t95 = Thread(target=scraper, args=[start_page + 94 * workload, start_page + 95 * workload, ])
    t96 = Thread(target=scraper, args=[start_page + 95 * workload, start_page + 96 * workload, ])
    t97 = Thread(target=scraper, args=[start_page + 96 * workload, start_page + 97 * workload, ])
    t98 = Thread(target=scraper, args=[start_page + 97 * workload, start_page + 98 * workload, ])
    t99 = Thread(target=scraper, args=[start_page + 98 * workload, start_page + 99 * workload, ])
    t100 = Thread(target=scraper, args=[start_page + 99 * workload, start_page + 100 * workload, ])
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()
    t31.start()
    t32.start()
    t33.start()
    t34.start()
    t35.start()
    t36.start()
    t37.start()
    t38.start()
    t39.start()
    t40.start()
    t41.start()
    t42.start()
    t43.start()
    t44.start()
    t45.start()
    t46.start()
    t47.start()
    t48.start()
    t49.start()
    t50.start()
    t51.start()
    t52.start()
    t53.start()
    t54.start()
    t55.start()
    t56.start()
    t57.start()
    t58.start()
    t59.start()
    t60.start()
    t61.start()
    t62.start()
    t63.start()
    t64.start()
    t65.start()
    t66.start()
    t67.start()
    t68.start()
    t69.start()
    t70.start()
    t71.start()
    t72.start()
    t73.start()
    t74.start()
    t75.start()
    t76.start()
    t77.start()
    t78.start()
    t79.start()
    t80.start()
    t81.start()
    t82.start()
    t83.start()
    t84.start()
    t85.start()
    t86.start()
    t87.start()
    t88.start()
    t89.start()
    t90.start()
    t91.start()
    t92.start()
    t93.start()
    t94.start()
    t95.start()
    t96.start()
    t97.start()
    t98.start()
    t99.start()
    t100.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()
    t25.join()
    t26.join()
    t27.join()
    t28.join()
    t29.join()
    t30.join()
    t31.join()
    t32.join()
    t33.join()
    t34.join()
    t35.join()
    t36.join()
    t37.join()
    t38.join()
    t39.join()
    t40.join()
    t41.join()
    t42.join()
    t43.join()
    t44.join()
    t45.join()
    t46.join()
    t47.join()
    t48.join()
    t49.join()
    t50.join()
    t51.join()
    t52.join()
    t53.join()
    t54.join()
    t55.join()
    t56.join()
    t57.join()
    t58.join()
    t59.join()
    t60.join()
    t61.join()
    t62.join()
    t63.join()
    t64.join()
    t65.join()
    t66.join()
    t67.join()
    t68.join()
    t69.join()
    t70.join()
    t71.join()
    t72.join()
    t73.join()
    t74.join()
    t75.join()
    t76.join()
    t77.join()
    t78.join()
    t79.join()
    t80.join()
    t81.join()
    t82.join()
    t83.join()
    t84.join()
    t85.join()
    t86.join()
    t87.join()
    t88.join()
    t89.join()
    t90.join()
    t91.join()
    t92.join()
    t93.join()
    t94.join()
    t95.join()
    t96.join()
    t97.join()
    t98.join()
    t99.join()
    t100.join()


def scraper(start, end):
    now = 0
    while True:
        if now < check_log(start, end):
            now = check_log(start, end)

        if now > end:
            break

        try:
            content = my_content(url + str(now))
            save_as_txt('theAthletic_' + str(now), content)
            save_log(start, end, now)
            now = now + 1
        except:
            time.sleep(10)
            pass




def my_content(my_url):

    print('scraping article in ' + my_url)
    try:
        res = requests.get(my_url, headers=headers).text
    except InterruptedError:
        time.sleep(10)
        res = requests.get(my_url, headers=headers).text
    content = BeautifulSoup(res, "html.parser")
    filecontent = "content"
    try:
        headline = content.find(attrs={'class': 'article-headline'}).text
        filecontent = headline
    except AttributeError:
        pass

    try:
        liveblog = content.find(attrs={'id':'live-blog-container'}).get_text(separator='\n')
        filecontent = liveblog

    except AttributeError:
        pass

    try:
        article = content.find(attrs={'id':'article-container-grid'}).get_text(separator='\n')
        filecontent = filecontent + article
    except AttributeError:
        pass

    filecontent = filecontent.replace('Advertisement\n', '')

    return filecontent


def save_as_txt(file_name, file_content):
    if (file_content != 'content') and (file_content[0:5] != 'Error'):
        # encode is needed on windows
        f = open(local_path + file_name+'.txt', 'w', encoding='UTF-8')
        f.write(file_content)
        f.close()

    else:
        pass

# for checking the progress on each thread:
# check_progress()

# start
if not os.path.exists(local_path):
    os.mkdir(local_path)

while True:

    my_count = 0
    print('in round:' + str(my_count))
    my_count = my_count + 1
    try:
        main()


    except KeyboardInterrupt:
        print('exit')
        time.sleep(3)
        break

    except:
        print("restarting...")
        time.sleep(3)
        pass
