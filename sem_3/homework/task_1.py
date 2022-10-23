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

# num = int(input("Enter the number: "))
#
#
# def create_list(n):
#     ls = []
#     for i in range(n):
#         rnd = random.choice(range(100))
#         ls.append(rnd)
#     return ls
#
#
# rnd_list = create_list(num)
# print(rnd_list)
#
#
# def even_ind_sum(ls, n):
#     res = 0
#     for i in range(n):
#         if i % 2 == 0:
#             res += ls[i]
#     return res
#
#
# even_ind_sum = even_ind_sum(rnd_list, num)
# print(even_ind_sum)
