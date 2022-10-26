from random import *

n = int(input("Enter the length for list: "))


def create_list(x):
    ls = [i for i in range(x + 1)]
    ls.remove(choice(ls))
    return ls


data = create_list(n)
print(data)


def find_miss_num(ls):
    for i in range(1, len(ls)):
        if ls[i] - 1 != ls[i-1]:
            return ls[i] - 1
    return -1


result = find_miss_num(data)
print(result)
