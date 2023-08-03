import requests
from bs4 import BeautifulSoup
import time
import os
import threading

#存储路径：local_path/20xx-xx-xx/title.txt
local_path = '/Users/hecate/Downloads/theAthletics/'
url = 'https://theathletic.com/sitemap.xml'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}

empty_links = []

page_links = [
    'https://theathletic.com/sitemap-pt-post-2023-07.xml',
    'https://theathletic.com/sitemap-pt-post-2023-06.xml',
    'https://theathletic.com/sitemap-pt-post-2023-05.xml',
    'https://theathletic.com/sitemap-pt-post-2023-04.xml',
    'https://theathletic.com/sitemap-pt-post-2023-03.xml',
    'https://theathletic.com/sitemap-pt-post-2023-02.xml',
    'https://theathletic.com/sitemap-pt-post-2023-01.xml',
    'https://theathletic.com/sitemap-pt-post-2022-12.xml',
    'https://theathletic.com/sitemap-pt-post-2022-11.xml',
    'https://theathletic.com/sitemap-pt-post-2022-10.xml',
    'https://theathletic.com/sitemap-pt-post-2022-09.xml',
    'https://theathletic.com/sitemap-pt-post-2022-08.xml',
    'https://theathletic.com/sitemap-pt-post-2022-07.xml',
    'https://theathletic.com/sitemap-pt-post-2022-06.xml',
    'https://theathletic.com/sitemap-pt-post-2022-05.xml',
    'https://theathletic.com/sitemap-pt-post-2022-04.xml',
    'https://theathletic.com/sitemap-pt-post-2022-03.xml',
    'https://theathletic.com/sitemap-pt-post-2022-02.xml',
    'https://theathletic.com/sitemap-pt-post-2022-01.xml',
    'https://theathletic.com/sitemap-pt-post-2021-12.xml',
    'https://theathletic.com/sitemap-pt-post-2021-11.xml',
    'https://theathletic.com/sitemap-pt-post-2021-10.xml',
    'https://theathletic.com/sitemap-pt-post-2021-09.xml',
    'https://theathletic.com/sitemap-pt-post-2021-08.xml',
    'https://theathletic.com/sitemap-pt-post-2021-07.xml',
    'https://theathletic.com/sitemap-pt-post-2021-06.xml',
    'https://theathletic.com/sitemap-pt-post-2021-05.xml',
    'https://theathletic.com/sitemap-pt-post-2021-04.xml',
    'https://theathletic.com/sitemap-pt-post-2021-03.xml',
    'https://theathletic.com/sitemap-pt-post-2021-02.xml',
    'https://theathletic.com/sitemap-pt-post-2021-01.xml',
    'https://theathletic.com/sitemap-pt-post-2020-12.xml',
    'https://theathletic.com/sitemap-pt-post-2020-11.xml',
    'https://theathletic.com/sitemap-pt-post-2020-10.xml',
    'https://theathletic.com/sitemap-pt-post-2020-09.xml',
    'https://theathletic.com/sitemap-pt-post-2020-08.xml',
    'https://theathletic.com/sitemap-pt-post-2020-07.xml',
    'https://theathletic.com/sitemap-pt-post-2020-06.xml',
    'https://theathletic.com/sitemap-pt-post-2020-05.xml',
    'https://theathletic.com/sitemap-pt-post-2020-04.xml',
    'https://theathletic.com/sitemap-pt-post-2020-03.xml',
    'https://theathletic.com/sitemap-pt-post-2020-02.xml',
    'https://theathletic.com/sitemap-pt-post-2020-01.xml',
    'https://theathletic.com/sitemap-pt-post-2019-12.xml',
    'https://theathletic.com/sitemap-pt-post-2019-11.xml',
    'https://theathletic.com/sitemap-pt-post-2019-10.xml',
    'https://theathletic.com/sitemap-pt-post-2019-09.xml',
    'https://theathletic.com/sitemap-pt-post-2019-08.xml',
    'https://theathletic.com/sitemap-pt-post-2019-07.xml',
    'https://theathletic.com/sitemap-pt-post-2019-06.xml',
    'https://theathletic.com/sitemap-pt-post-2019-05.xml',
    'https://theathletic.com/sitemap-pt-post-2019-04.xml',
    'https://theathletic.com/sitemap-pt-post-2019-03.xml',
    'https://theathletic.com/sitemap-pt-post-2019-02.xml',
    'https://theathletic.com/sitemap-pt-post-2019-01.xml',
    'https://theathletic.com/sitemap-pt-post-2018-12.xml',
    'https://theathletic.com/sitemap-pt-post-2018-11.xml',
    'https://theathletic.com/sitemap-pt-post-2018-10.xml',
    'https://theathletic.com/sitemap-pt-post-2018-09.xml',
    'https://theathletic.com/sitemap-pt-post-2018-08.xml',
    'https://theathletic.com/sitemap-pt-post-2018-07.xml',
    'https://theathletic.com/sitemap-pt-post-2018-06.xml',
    'https://theathletic.com/sitemap-pt-post-2018-05.xml',
    'https://theathletic.com/sitemap-pt-post-2018-04.xml',
    'https://theathletic.com/sitemap-pt-post-2018-03.xml',
    'https://theathletic.com/sitemap-pt-post-2018-02.xml',
    'https://theathletic.com/sitemap-pt-post-2018-01.xml',
    'https://theathletic.com/sitemap-pt-post-2017-12.xml',
    'https://theathletic.com/sitemap-pt-post-2017-11.xml',
    'https://theathletic.com/sitemap-pt-post-2017-10.xml',
    'https://theathletic.com/sitemap-pt-post-2017-09.xml',
    'https://theathletic.com/sitemap-pt-post-2017-08.xml',
    'https://theathletic.com/sitemap-pt-post-2017-07.xml',
    'https://theathletic.com/sitemap-pt-post-2017-06.xml',
    'https://theathletic.com/sitemap-pt-post-2017-05.xml',
    'https://theathletic.com/sitemap-pt-post-2017-04.xml',
    'https://theathletic.com/sitemap-pt-post-2017-03.xml',
    'https://theathletic.com/sitemap-pt-post-2017-02.xml',
    'https://theathletic.com/sitemap-pt-post-2017-01.xml',
    'https://theathletic.com/sitemap-pt-post-2016-12.xml',
    'https://theathletic.com/sitemap-pt-post-2016-11.xml',
    'https://theathletic.com/sitemap-pt-post-2016-10.xml',
    'https://theathletic.com/sitemap-pt-post-2016-09.xml',
    'https://theathletic.com/sitemap-pt-post-2016-08.xml',
    'https://theathletic.com/sitemap-pt-post-2016-07.xml',
    'https://theathletic.com/sitemap-pt-post-2016-06.xml',
    'https://theathletic.com/sitemap-pt-post-2016-05.xml',
    'https://theathletic.com/sitemap-pt-post-2016-04.xml',
    'https://theathletic.com/sitemap-pt-post-2016-03.xml',
    'https://theathletic.com/sitemap-pt-post-2016-02.xml',
    'https://theathletic.com/sitemap-pt-post-2016-01.xml',
    'https://theathletic.com/sitemap-pt-post-2000-08.xml',
]

counter = 0

def scraper(my_link):
    links = get_content_links(my_link)

    parent_link = my_link.replace('https://theathletic.com/', '')

    initiate_log(parent_link)
    for link in links:
        link = link.replace('<loc>', '')
        link = link.replace('</loc>', '')
        if check_log(parent_link, link) == -1:
            if link != empty_links:
                save_as_txt(parent_link,
                            link.replace('https://theathletic.com/', '').replace('/', ''),
                            my_content(link))
                write_log(parent_link, link)

                global counter
                counter = counter + 1
                print('current work:' + str(counter))

            else:
                print('emptylink:' + link)
        else:
            print('contentlink has been scrapped:' + link)


def initiate_log(path):
    if os.path.exists(local_path + path):
        print('exist')
    else:
        print('making path')
        os.mkdir(local_path + path)
        file = open(local_path + path + '/log.txt', 'w')
        print('file made')
        file.close()


def write_log(path, link):

    f = open(local_path + path + '/log.txt', 'a')
    f.write(link + '\n')


def check_log(path, link):

    f = open(local_path + path + '/log.txt', 'r')
    print("finding link in log:" + link)

    if f.read().find(link) == -1:
        f.close()
        return -1;

    else:
        f.close()
        return 1


def get_content_links(post_url):
    print("processing posturl:" + post_url)

    try:
        res = requests.get(post_url, headers=headers).text
    except InterruptedError:
        time.sleep(100)
        res = requests.get(post_url, headers=headers).text
    strlinks = []
    content = BeautifulSoup(res, "html.parser")

    try:
        links = content.findAll(name='loc')
    except:
        return strlinks

    for link in links:
        strlinks.append(str(link))



    return strlinks


def get_post_links(sitemap_url):
    try:
        res = requests.get(sitemap_url, headers=headers).text
    except InterruptedError:
        time.sleep(100)
        res = requests.get(sitemap_url, headers=headers).text
    content = BeautifulSoup(res, "html.parser")
    links = content.findAll(name='loc')
    strlinks = []
    for link in links:
        strlinks.append(str(link))

    return strlinks


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
        headline = content.find(attrs={'class':'article-headline'}).text
        filecontent = headline
    except AttributeError:
        print('no headline')

    try:
        liveblog = content.find(attrs={'id':'live-blog-container'}).text
        filecontent = liveblog

    except AttributeError:
        print('no headline')

    try:
        article = content.find(attrs={'id':'article-container-grid'}).text
        filecontent = filecontent + article
    except AttributeError:
        print('no article')


    return filecontent


def save_as_txt(file_path, file_name, file_content):
    if os.path.exists(local_path + file_path):
        a = 1
    else:
        os.mkdir(local_path + file_path)
    f = open(local_path + file_path + '/' + file_name+'.txt', 'w')
    f.write(file_content)
    f.close()


print(len(page_links))

t0 = threading.Thread(target=scraper, args=(page_links[0], ))
t1 = threading.Thread(target=scraper, args=(page_links[1], ))
t2 = threading.Thread(target=scraper, args=(page_links[2], ))
t3 = threading.Thread(target=scraper, args=(page_links[3], ))
t4 = threading.Thread(target=scraper, args=(page_links[4], ))
t5 = threading.Thread(target=scraper, args=(page_links[5], ))
t6 = threading.Thread(target=scraper, args=(page_links[6], ))
t7 = threading.Thread(target=scraper, args=(page_links[7], ))
t8 = threading.Thread(target=scraper, args=(page_links[8], ))
t9 = threading.Thread(target=scraper, args=(page_links[9], ))
t10 = threading.Thread(target=scraper, args=(page_links[10], ))
t11 = threading.Thread(target=scraper, args=(page_links[11], ))
t12 = threading.Thread(target=scraper, args=(page_links[12], ))
t13 = threading.Thread(target=scraper, args=(page_links[13], ))
t14 = threading.Thread(target=scraper, args=(page_links[14], ))
t15 = threading.Thread(target=scraper, args=(page_links[15], ))
t16 = threading.Thread(target=scraper, args=(page_links[16], ))
t17 = threading.Thread(target=scraper, args=(page_links[17], ))
t18 = threading.Thread(target=scraper, args=(page_links[18], ))
t19 = threading.Thread(target=scraper, args=(page_links[19], ))
t20 = threading.Thread(target=scraper, args=(page_links[20], ))
t21 = threading.Thread(target=scraper, args=(page_links[21], ))
t22 = threading.Thread(target=scraper, args=(page_links[22], ))
t23 = threading.Thread(target=scraper, args=(page_links[23], ))
t24 = threading.Thread(target=scraper, args=(page_links[24], ))
t25 = threading.Thread(target=scraper, args=(page_links[25], ))
t26 = threading.Thread(target=scraper, args=(page_links[26], ))
t27 = threading.Thread(target=scraper, args=(page_links[27], ))
t28 = threading.Thread(target=scraper, args=(page_links[28], ))
t29 = threading.Thread(target=scraper, args=(page_links[29], ))
t30 = threading.Thread(target=scraper, args=(page_links[30], ))
t31 = threading.Thread(target=scraper, args=(page_links[31], ))
t32 = threading.Thread(target=scraper, args=(page_links[32], ))
t33 = threading.Thread(target=scraper, args=(page_links[33], ))
t34 = threading.Thread(target=scraper, args=(page_links[34], ))
t35 = threading.Thread(target=scraper, args=(page_links[35], ))
t36 = threading.Thread(target=scraper, args=(page_links[36], ))
t37 = threading.Thread(target=scraper, args=(page_links[37], ))
t38 = threading.Thread(target=scraper, args=(page_links[38], ))
t39 = threading.Thread(target=scraper, args=(page_links[39], ))
t40 = threading.Thread(target=scraper, args=(page_links[40], ))
t41 = threading.Thread(target=scraper, args=(page_links[41], ))
t42 = threading.Thread(target=scraper, args=(page_links[42], ))
t43 = threading.Thread(target=scraper, args=(page_links[43], ))
t44 = threading.Thread(target=scraper, args=(page_links[44], ))
t45 = threading.Thread(target=scraper, args=(page_links[45], ))
t46 = threading.Thread(target=scraper, args=(page_links[46], ))
t47 = threading.Thread(target=scraper, args=(page_links[47], ))
t48 = threading.Thread(target=scraper, args=(page_links[48], ))
t49 = threading.Thread(target=scraper, args=(page_links[49], ))
t50 = threading.Thread(target=scraper, args=(page_links[50], ))
t51 = threading.Thread(target=scraper, args=(page_links[51], ))
t52 = threading.Thread(target=scraper, args=(page_links[52], ))
t53 = threading.Thread(target=scraper, args=(page_links[53], ))
t54 = threading.Thread(target=scraper, args=(page_links[54], ))
t55 = threading.Thread(target=scraper, args=(page_links[55], ))
t56 = threading.Thread(target=scraper, args=(page_links[56], ))
t57 = threading.Thread(target=scraper, args=(page_links[57], ))
t58 = threading.Thread(target=scraper, args=(page_links[58], ))
t59 = threading.Thread(target=scraper, args=(page_links[59], ))
t60 = threading.Thread(target=scraper, args=(page_links[60], ))
t61 = threading.Thread(target=scraper, args=(page_links[61], ))
t62 = threading.Thread(target=scraper, args=(page_links[62], ))
t63 = threading.Thread(target=scraper, args=(page_links[63], ))
t64 = threading.Thread(target=scraper, args=(page_links[64], ))
t65 = threading.Thread(target=scraper, args=(page_links[65], ))
t66 = threading.Thread(target=scraper, args=(page_links[66], ))
t67 = threading.Thread(target=scraper, args=(page_links[67], ))
t68 = threading.Thread(target=scraper, args=(page_links[68], ))
t69 = threading.Thread(target=scraper, args=(page_links[69], ))
t70 = threading.Thread(target=scraper, args=(page_links[70], ))
t71 = threading.Thread(target=scraper, args=(page_links[71], ))
t72 = threading.Thread(target=scraper, args=(page_links[72], ))
t73 = threading.Thread(target=scraper, args=(page_links[73], ))
t74 = threading.Thread(target=scraper, args=(page_links[74], ))
t75 = threading.Thread(target=scraper, args=(page_links[75], ))
t76 = threading.Thread(target=scraper, args=(page_links[76], ))
t77 = threading.Thread(target=scraper, args=(page_links[77], ))
t78 = threading.Thread(target=scraper, args=(page_links[78], ))
t79 = threading.Thread(target=scraper, args=(page_links[79], ))
t80 = threading.Thread(target=scraper, args=(page_links[80], ))
t81 = threading.Thread(target=scraper, args=(page_links[81], ))
t82 = threading.Thread(target=scraper, args=(page_links[82], ))
t83 = threading.Thread(target=scraper, args=(page_links[83], ))
t84 = threading.Thread(target=scraper, args=(page_links[84], ))
t85 = threading.Thread(target=scraper, args=(page_links[85], ))
t86 = threading.Thread(target=scraper, args=(page_links[86], ))
t87 = threading.Thread(target=scraper, args=(page_links[87], ))
t88 = threading.Thread(target=scraper, args=(page_links[88], ))
t89 = threading.Thread(target=scraper, args=(page_links[89], ))
t90 = threading.Thread(target=scraper, args=(page_links[90], ))
t91 = threading.Thread(target=scraper, args=(page_links[91], ))

t0.start()
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






