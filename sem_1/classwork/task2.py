# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

max_num = 0
for i in range(5):
    a = int(input('enter the number: '))
    if a > max_num:
        max_num = a
print(max_num)
