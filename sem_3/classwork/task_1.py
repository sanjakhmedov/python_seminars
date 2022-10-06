import random

size = int(input('enter the value for size of list: '))
num = int(input('enter the number: '))


def check_num(s, n):
    if n < 0:
        return print('Error')
    ls = random.sample(range(s * 2), s)
    print(ls)

    if n in ls:
        return print('YES')
    return print('NO')


check_num(size, num)
