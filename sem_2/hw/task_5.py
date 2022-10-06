# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
from hashlib import new
from random import random

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for i in range(10):
    temp_rnd = round(random() * 10)
    if temp_rnd == arr[i]:
        continue
    else:
        arr[i] = temp_rnd


print(arr)
