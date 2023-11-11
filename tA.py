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
