# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

n = int(input('enter the value for N: '))

print(*range(-n, n + 1))

