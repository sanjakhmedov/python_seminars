from random import *


def create_list(s, item1):
    ls = []
    for i in range(s):
        temp = choices(item1, k=3)
        ls.append("".join(temp))
    return ls


def remove_elem(ls, d):
    temp = ls
    if temp.count(d) <= 0:
        return "There is no such element in this list!!!"
    else:
        temp.remove(d)
        return temp


size = int(input("Enter the list length: "))
item = input("Enter the letters without spaces: ")
rnd_list = create_list(size, item)
print(rnd_list)
search = input("Enter the item to remove: ")
res = remove_elem(rnd_list, search)
print(res)
