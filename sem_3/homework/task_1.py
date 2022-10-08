# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

import random


def random_list(n, minimum, maximum):
    if n < 0:
        return "please enter the positive number!!!"
    ls = []
    for i in range(n):
        ls.append(round(random.uniform(minimum, maximum)))
    return ls


def sum_even_index(ls):
    res = 0
    for i in range(num):
        if i % 2 == 0:
            res += ls[i]
    return res


num = int(input('Enter the length of list: '))
least = int(input('Enter the minimum range: '))
most = int(input('Enter the maximum range: '))

rnd_ls = random_list(num, least, most)
print(rnd_ls)

sum_result = sum_even_index(rnd_ls)
print(sum_result)
