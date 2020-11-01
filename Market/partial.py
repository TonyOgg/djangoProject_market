# 1. Найти функцию которая принимает несколько аргументов.
#    - С помощью partial передать часть (не все) аргументы в найденную функцию создав новую.
#    - Передать остаток аргументов получив результат вычисления

from functools import partial as par


def multiplier(first, second):
    return first * second


part_1 = par(multiplier, 3, 4)
print(part_1)
print(part_1())