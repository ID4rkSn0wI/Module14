
print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0 or y_diff == 0:
    k = 0
else:
    k = y_diff / x_diff
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)

# TODO нужно делать уонструкцию вида if elif else
# TODO где в первых двух будем обработка если x_diff = 0 во втором y_diff = 0
# TODO при входных данных 10 20 и 10 45 ответ x = 10.0
