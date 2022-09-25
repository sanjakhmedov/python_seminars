x = int(input('enter the coordinates for x: '))
y = int(input('and y: '))


def find_quarter(x1, y1):
    if x1 > 0 and y1 > 0:
        print(1)
    elif x1 < 0 and y1 > 0:
        print(2)
    elif x1 < 0 and y1 < 0:
        print(3)
    elif x1 > 0 and y1 < 0:
        print(4)
    else:
        print('Error, 0 entered!')


find_quarter(x, y)
