import time


# url = 'https://theathletic.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35'}

const_local_path = '/Users/hecate/Downloads/BR/'

start_page = int(140000)
end_page = int(10100000)

local_path = const_local_path + str(start_page) + '_to_' + str(end_page) + '/'

def check_progress():
    workload = int((end_page - start_page) / 100)

    for i in range(1, 101):
        filename = local_path + 'log_' + str(start_page + (i - 1) * workload) + '_' + str(
            start_page + i * workload) + '.txt'

        f = open(filename, 'r')

        now = int(f.readline().rstrip())

        percentage = (int(now) - start_page - (i - 1) * workload) / workload * 100

        print('Thread ' + str(i) + ': ' + str(now) + ' / ' + str(start_page + i * workload) + ' Progress: ' + str(
            percentage) + '%')

    time.sleep(5)

check_progress()
