def calculate_sum_of_numerals(number):
    sum_of_numerals = 0
    temp = number
    sum_of_numerals += temp % 10
    while temp > 0:
        if temp // 10 > 0:
            sum_of_numerals += temp % 10
        else:
            sum_of_numerals += temp % 10
            break
        temp //= 10
    return sum_of_numerals


def calculate_amount_of_numerals(number):
    amount_of_numerals = 0
    temp = number
    amount_of_numerals += 1
    while temp != 0:
        if temp // 10 > 0:
            amount_of_numerals += 1
        else:
            break
        temp //= 10
    return amount_of_numerals


N_number = int(input("Введите целое положительное число: "))
sum_of_numeral = calculate_sum_of_numerals(N_number)
amount_of_numeral = calculate_amount_of_numerals(N_number)
print("Сумма цифр:", sum_of_numeral)
print("Кол-во цифр в числе:", amount_of_numeral)
difference = sum_of_numeral - amount_of_numeral
print("Разность суммы и кол-ва цифр:", difference)
