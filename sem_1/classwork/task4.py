a = float(input('введите вещественное число: '))
a = a * 10 % 10
if a != 0:
    print(int(a))
else:
    print('no')
