# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy int this form '0.0001': 0.000001
#
# out
# 9.000000

from random import *
from decimal import *

getcontext().prec = 6
print(Decimal(1) / Decimal(7))
Decimal('0.142857')
getcontext().prec = 28
print(Decimal(1) / Decimal(7))
