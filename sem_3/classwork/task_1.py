import random

# size = int(input('enter the value for size of list: '))
# num = int(input('enter the number: '))
#
#
# def check_num(s, n):
#     if n < 0:
#         return print('Error')
#     ls = random.sample(range(s * 2), s)
#     print(ls)
#
#     if n in ls:
#         return print('YES')
#     return print('NO')
#
#
# check_num(size, num)

list_length = int(input('Indicate the list length: '))
num = int(input('Enter the number: '))


def create_list(size):
    if size <= 0:
        return 'Error'
    nums = random.sample(range(size * 2), size)
    return nums


def is_num_in_list(n_list, n):
    if n in n_list:
        return 'Yes'
    return 'No'


ls = create_list(list_length)
print(ls)
result = is_num_in_list(ls, num)
print(result)

