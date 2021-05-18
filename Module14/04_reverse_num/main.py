def calculate_numbers(number):
    reserve_number = ""
    while number > 0:
        temp = number % 10
        if number > 0:
            reserve_number += str(temp)
        number //= 10
    return int(reserve_number)


first_number = int(input("\nВведите первое число: "))
second_number = int(input("Введите второе число: "))
first_reserve_number = calculate_numbers(first_number)
second_reserve_number = calculate_numbers(second_number)
print("\nПервое число наоборот:", first_reserve_number)
print("Второе число наоборот:", second_reserve_number)
sum_of_reserve_numbers = first_reserve_number + second_reserve_number
print("Сумма:", sum_of_reserve_numbers)
