# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

from random import choices


def create_rnd_ls(count1, source1):
    result = []
    for i in range(count1):
        temp = choices(source1, k=3)
        result.append(''.join(temp))
    return result



def find_second_intercourse(word1, words_list1):
    if words_list1.count(word1) > 1:
        first_ent = words_list1.index(word1)
        print(f'second intercourse: {words_list1.index(word1, first_ent + 1)}')
    else:
        print('-1')




count, source = int(input('enter the count value: ')), input('enter the source value: ')

words = create_rnd_ls(count, source)
print(words)

find_second_intercourse(input(), words)
