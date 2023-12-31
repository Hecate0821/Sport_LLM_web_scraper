const_local_path = './espnArticles/'

start_page = int(500)
end_page = int(38200500)

local_path = const_local_path + str(start_page) + '_to_' + str(end_page) + '/'

thread_num = int(500)

def check_progress():
    workload = int((end_page - start_page) / thread_num)

    for i in range(1, thread_num+1):
        log_path = local_path + 'log/'
    
        filename = log_path + 'log_' + str(start_page + (i - 1) * workload) + '_' + str(
            start_page + i * workload) + '.txt'

        f = open(filename, 'r')

        now = int(f.readline().rstrip())

        percentage = (int(now) - start_page - (i - 1) * workload) / workload * 100

        print('Thread ' + str(i) + ': ' + str(now) + ' / ' + str(start_page + i * workload) + ' Progress: ' + str(
            percentage) + '%')


check_progress()
