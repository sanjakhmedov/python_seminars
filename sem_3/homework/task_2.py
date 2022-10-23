# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
#
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
#
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

import random


num = int(input("Enter the number: "))


def create_list(n):
    ls = []
    for i in range(n):
        rnd = random.choice(range(10))
        ls.append(rnd)
    return ls


rnd_list = create_list(num)
print(rnd_list)


def mult_pair_elem(ls, n):
    res = []
    if n % 2 == 0:
        for i in range(n//2):
            res.append(ls[i] * ls[n - i - 1])
    else:
        for i in range(n//2):
            res.append(ls[i] * ls[n - i - 1])
    res.append(ls[n//2])
    return res


mult_pair_elem = mult_pair_elem(rnd_list, num)
print(mult_pair_elem)
