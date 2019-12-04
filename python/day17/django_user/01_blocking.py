from time sleep

def sleep_3s():
    sleep(3)
    print('3초 끝')

def run_time():
    print('시작')
    sleep_3s()
    print('끝')

    run_time()
