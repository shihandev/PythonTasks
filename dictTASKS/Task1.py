def is_in_interval(number):
    if (-15 < number <= 12) or (14 < number < 17) or (number >= 19):
        return True
    else:
        return False

# Пример использования:
input_number = int(input("Введите целое число: "))
result = is_in_interval(input_number)
print(result)
