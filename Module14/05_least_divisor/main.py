def min_divider(n, d):
    if n % d == 0 and n > 1:
        return d
    else:
        min_divider(n, d + 1)


number = int(input("Введите число: "))
if number > 1:
    d = 2
    min_divider_of_number = min_divider(number, d)
    print("Наименьший делитель, отличный от единицы:", min_divider_of_number)
else:
    print("Нет делителя, отличного от единицы. Попробуйте снова")
