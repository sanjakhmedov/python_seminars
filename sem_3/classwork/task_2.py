# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

import random
from random import choices


# def create_rnd_ls(count1, source1):
#     result = []
#     for i in range(count1):
#         temp = choices(source1, k=3)
#         result.append(''.join(temp))
#     return result
#
#
#
# def find_second_intercourse(word1, words_list1):
#     if words_list1.count(word1) > 1:
#         first_ent = words_list1.index(word1)
#         print(f'second intercourse: {words_list1.index(word1, first_ent + 1)}')
#     else:
#         print('-1')
#
#
#
#
# count, source = int(input('enter the count value: ')), input('enter the source value: ')
#
# words = create_rnd_ls(count, source)
# print(words)
#
# find_second_intercourse(input(), words)


size = int(input("Enter the list length: "))
item = input("Enter the letters without spaces: ")


def create_list(s, item1):
    ls = []
    for i in range(s):
        temp = choices(item1, k=3)
        ls.append("".join(temp))
    return ls


rnd_list = create_list(size, item)
search = input("Enter the search item: ")


def check_second_intercourse(ls, word):
    if ls.count(word) > 1:
        ent_one = ls.index(word)
        print(f"Second intercourse: {ls.index(word, ent_one + 1)}")
    else:
        print(-1)


print(rnd_list)
check_second_intercourse(rnd_list, search)


