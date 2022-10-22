# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

num = int(input("Enter the number: "))


def create_list(n):
    ls = []
    for i in range(n):
        rnd = round(random.uniform(0, 10), 2)
        ls.append(rnd)
    return ls


rnd_list = create_list(num)
print(rnd_list)


def min_max_after_dot(ls, n):
    res = []
    for i in range(n):
        while ls[i] == 0:
            temp = ls[i] * 10
    return res


print(min_max_after_dot(rnd_list, num))
