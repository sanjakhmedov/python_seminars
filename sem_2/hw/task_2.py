num = int(input('Enter the number: '))

res = 1
for i in range(1, num + 1):
    print(res, end=' ')
    res += res * i
