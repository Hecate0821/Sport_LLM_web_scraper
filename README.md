# Sport_LLM_web_scraper
Scrapers for sports articles

## Scraper
Template.py
根据修改get_content function
对于错误的页面内容，需要return 'error:' + 错误类型 + 其他信息
需要重试的状态码写在:
retry_code
需要跳过的状态码写在:
skip_code

## Checker
to check progress:
python3 scraper.py -p
