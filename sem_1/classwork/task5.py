a = int(input('Enter the number: '))
if (a % 10 == 0 or a % 15 == 0) and (a % 30 != 0):
    print('yes')
else:
    print('no')
