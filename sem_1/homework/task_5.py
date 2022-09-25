import math

x1 = float(input('enter the value for point A. \nx: '))
y1 = float(input('y: '))
x2 = float(input('enter the value for point B. \nx: '))
y2 = float(input('y: '))

print(round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 4))

