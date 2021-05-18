def if_coin_in_square(x_coordinate, y_coordinate):
    return (start_of_circle >= x_coordinate >= end_of_circle) and (end_of_circle <= y_coordinate <= start_of_circle)


point_x = float(input("Введите координату x: "))
point_y = float(input("Введите координату x: "))
start_of_circle = float(input("Введите радиус круга: "))
end_of_circle = start_of_circle - 2 * start_of_circle
if if_coin_in_square(point_x, point_y):
    print("\nМонетка где-то рядом")
else:
    print("\nМонетки в области нет")
