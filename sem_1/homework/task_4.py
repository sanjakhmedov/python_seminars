x = int(input('Enter the quarter: '))


def find_range(x1):
    if x1 == 1:
        print('(x > 0, y > 0)')
    elif x1 == 2:
        print('(x < 0, y > 0)')
    elif x1 == 3:
        print('(x < 0, y < 0)')
    elif x1 == 4:
        print('(x > 0, y < 0)')
    else:
        print('Incorrect quarter entered!')


find_range(x)
