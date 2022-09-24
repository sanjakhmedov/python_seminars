# 1. Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.

a = int(input('Enter the number for "a": '))
b = int(input('Enter the number for "b": '))

if a * a == b or b * b == a:
    print('yes')
else:
    print('no')
