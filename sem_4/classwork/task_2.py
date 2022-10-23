# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

# ax**2 + bx + c = 0
#
# D = b**2 − 4ac
#
# если D < 0, корней нет;
# если D = 0, есть один корень;
# если D > 0, есть два различных корня.


from math import sqrt

print("Enter the values for ")
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

d = b ** 2 - 4 * a * c

with open("temp.txt", "a", encoding="utf-8") as result:
    result.write(f"equation: {a}*x^2 + {b}*x + {c} \n")
    #    def quadratic_equation(a, b, c):
    if d > 0 and a:
        x1 = round((-b + sqrt(d)) / (2 * a), 2)
        x2 = round((-b - sqrt(d)) / (2 * a), 2)
        result.write(f"roots: {x1}, {x2} \n")
    elif int(d) == 0:
        x = round(-b / (2 * a), 2)
        result.write(f"the only root: {x} \n")
    else:
        result.write("no roots \n")
