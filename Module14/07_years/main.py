def calculate_years(start_of_function, end_of_function):
    for year in range(start_of_function, end_of_function + 1):
        quantity_of_numbers = 1
        temp = year
        first_temp = temp % 10
        second_temp = (temp // 10) % 10
        temp //= 100
        if first_temp == second_temp:
            quantity_of_numbers += 1
            if temp % 10 == first_temp or temp % 10 == second_temp or (temp // 10) % 10 == first_temp or (temp // 10) % 10 == second_temp:
                quantity_of_numbers += 1
                print(year)
        else:
            if temp % 10 == first_temp and (temp // 10) % 10 == first_temp:
                print(year)
            if temp % 10 == second_temp and (temp // 10) % 10 == second_temp:
                print(year)


start = int(input("Введите первый год: "))
stop = int(input("Введите второй год: "))
print("Года от 1900 до 2100 с тремя одинаковыми цифрами:")
calculate_years(start, stop)

