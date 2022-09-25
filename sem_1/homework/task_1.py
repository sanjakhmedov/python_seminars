n = int(input('enter the number: '))


def check_week_day(a):
    if 1 <= a <= 5:
        print('yes')
    elif 6 <= a <= 7:
        print('no')
    else:
        print('not a day of the week!')


check_week_day(n)
