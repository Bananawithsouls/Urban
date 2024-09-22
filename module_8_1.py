def add_everything_up(a, b):
    if type(a) == str or type(b) == str:
        # Если один из аргументов - строка, возвращаем их строковое представление
        return str(a) + str(b)
    else:
        # Если оба аргумента - числа, складываем их
        return a + b


print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Вывод: 130.456
