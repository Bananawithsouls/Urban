def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Отделяем первую цифру и преобразуем её в целое число
    first = int(str_number[0])

    # Если длина строки меньше или равна 1, возвращаем само число
    if len(str_number) <= 1:
        return int(str_number)

    # Рекурсивно вызываем функцию для оставшейся части строки
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример результата выполнения программы:
result = get_multiplied_digits(40203)
print(result)
