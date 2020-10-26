# # 1. Написать функцию которая будет распаковывать цифры 7 и 6 в переменные x и y из списка
# # ls = [4,[7,8],6]    Использовать unboxing.
#
# ls = [4, [7, 8], 6]
#
# def unboxing_1(ls):
#     x, _ = ls[1]
#     y = ls[2]
#     print(x + y)
#
# unboxing_1(ls)
#
# # 2. Написать функцию которая будет бежать for-ом по списку  ls = [ (3, [9, 1]), [(23,43), [5, 4]] ]
# # и суммировать элементы 9 и 5 используя unboxing.
#
# ls1 = [(3, [9, 1]), [(23, 43), [5, 4]]]
#
#
# def unboxing_2(ls):
#     y = 0
#     for (_, (x, _)) in ls:
#         y += x
#     print(y)
#
#
# unboxing_2(ls1)

import time
import random
from datetime import datetime

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n
#
# def lazy_generator_of_six(fn, num_of_iters):
#     ls = []
#     while len(ls) != 6:
#         pr_number = random.randint(1, num_of_iters)
#         if IsPrime(pr_number):
#             ls.append(pr_number)
#     yield ls


# start = datetime.now()
# print(next(lazy_generator_of_six(IsPrime, 10000)))
# print('Время выполнения' + ' ' + str((datetime.now() - start).total_seconds()))

class Lazy_iterator():

    def __init__(self, fn, num):
        self.fn = fn
        self.num = num
        self.ls = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.ls) > 6:
            raise StopIteration()
        else:
            while len(self.ls) != 6:
                pr_number = random.randint(1, self.num)
                if self.fn(pr_number):
                    self.ls.append(pr_number)
            return self.ls


start = datetime.now()
iterator = Lazy_iterator(IsPrime, 5)
print(next(iterator))
print(next(iterator))
print('Время выполнения' + ' ' + str((datetime.now() - start).total_seconds()))