# 3. Задайте два числа. Напишите программу, которая найдёт
# НОК (наименьшее общее кратное) этих двух чисел.
from math import gcd, lcm

print("Enter the number for the following variables ")
a = int(input("a: "))
b = int(input("b: "))


def nok(a1, b1):
    return (a1 * b1) // gcd(a1, b1)


print(nok(a, b))
