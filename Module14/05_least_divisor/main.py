def calculate_least_divisor(divisor_number, divisor):
    if divisor_number % divisor == 0:
        return divisor
    else:
        least_divisor(divisor_number, divisor + 1)


number = int(input("Введите число: "))
if number > 1:
    divisor = 2
    least_divisor = calculate_least_divisor(number, divisor)
    print("Наименьший делитель, отличный от единицы:", least_divisor)
else:
    print("Нет делителя, отличного от единицы. Попробуйте снова")
