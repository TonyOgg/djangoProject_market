import time
import random
import threading


def api(result):
    time.sleep(1)
    result['key'] = random.randint(1, 100)

def fn1():
    a = {}
    st = time.time()
    for i in range(5):
        api(a)
    return time.time() - st

print(fn1())

def experiment():
    st = time.time()
    threads = []
    for _ in range(4):
        result = {}
        t = threading.Thread(target=api, args=(result,))
        t.start()
        threads.append([t, result])
    thread_number = 1
    for thread, result in threads:
        thread.join()
        print("Поток " + str(thread_number) + ' вернул ' + str(result['key']))
        thread_number = thread_number + 1
    print(time.time() - st)

experiment()