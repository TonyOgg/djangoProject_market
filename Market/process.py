import traceback
import pickle
import random
import math

from datetime import datetime
from multiprocessing import Process, Pipe


def process_wrapper(fn, child_conn, *args, **kwargs):
    try:
        result = fn(*args, **kwargs)
    except Exception as e:
        msg = "Exception message: " + str(e) + "\n" + "Traceback: " + traceback.format_exc()
        print(msg)
        result = msg

    result = pickle.dumps(result, protocol=pickle.HIGHEST_PROTOCOL)
    child_conn.send_bytes(result)


def run(ls):
    start = datetime.now()
    tmp = []
    for fn, args, kwargs in ls:
        parent_conn, child_conn = Pipe()
        p = Process(target=process_wrapper, args=(fn, child_conn) + args, kwargs=kwargs)
        p.start()
        tmp.append(
            (p, parent_conn, child_conn)
        )

    result = []
    for p, parent_conn, child_conn in tmp:
        result.append(parent_conn.recv_bytes())
        p.join()
        parent_conn.close()
        child_conn.close()

    execution_time = datetime.now() - start
    print("Время работы: " + str(execution_time.total_seconds()) + ' секунд')

    return result


def each_slice(ls, size: int):
    start = 0
    finish = size
    slice = ls[start:finish]
    result = []
    while slice != []:
        result.append(slice)
        start = finish
        finish = start + size
        slice = ls[start:finish]

    return result


def create_random_list(ls):
    result = []
    for x in ls:
        x = (x / 34) * 41
        if x > 500:
            x = x ** 10
        result.append(x)
    return result


def example1():
    size = 100000
    ls = []
    for _ in range(size):
        ls.append(random.randint(1, 100))

    run([[create_random_list, (ls,), {}]])

    processes_number = 2
    tasks = []
    for slice in each_slice(ls, int(size / processes_number)):
        tasks.append(
            [create_random_list, (slice,), {}]
        )
    run(tasks)

def ls():
    a = []
    size = 1000000
    for _ in range(size):
        a.append(random.randint(1, 100))
    return a

def fack(p):
    a = []
    for i in p:
        a.append(math.factorial(i))
    return a


def example2():
    size = 1000000
    ls = []
    for _ in range(size):
        ls.append(random.randint(1, 100))

    run([[fack, (ls,), {}]])

    processes_number = 2
    tasks = []
    for slice in each_slice(ls, int(size / processes_number)):
        tasks.append(
            [fack, (slice,), {}]
        )
    run(tasks)

example2()