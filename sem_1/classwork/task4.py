a = float(input('введите вещественное число: '))
if a * 10 % 10 != 0:
    print(round(a * 10 // 1 % 10))
else:
    print('no')
