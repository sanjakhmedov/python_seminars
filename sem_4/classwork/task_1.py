n = input("Enter the number with space: ").split()


def is_num(val):
    for i in val:
        if not i.replace("-", "").isdigit():
            return []
    return val


value = is_num(n)


def min_max(a):
    if a:
        return min(a, key=int), max(a, key=int)
    else:
        return []


result = min_max(value)
print(value)
print(result)
