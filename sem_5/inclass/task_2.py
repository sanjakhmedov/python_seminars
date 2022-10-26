from random import *

size = int(input("Give the length for list: "))
print("Give range to pick random numbers ")
minimal = int(input("Min: "))
maximal = int(input("Max: "))


def create_list(s, least, most):
    return [choice(range(least, most)) for i in range(s)]


def order_sublist(ls):
    res = []
    for i in range(len(ls)):
        temp = ls[i]
        temp_ls = [temp]
        for j in range(i, len(ls)):
            if ls[j] > temp:
                temp_ls.append(ls[j])
                temp = ls[j]
        if len(temp_ls) > 1:
            res.append(temp_ls)
    return res


rnd_list = create_list(size, minimal, maximal)
print(rnd_list)
print(order_sublist(rnd_list))
