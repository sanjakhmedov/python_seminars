# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy int this form '0.0001': 0.000001
#
# out
# 9.000000

from random import *
from decimal import *


def accuracy(num, acc):
    number = Decimal(f"{num}")
    return number.quantize(Decimal(f"{acc}"))


print(accuracy(float(input("Enter an actual number: ")), float(input("Enter the required accuracy 0.0001: "))))
