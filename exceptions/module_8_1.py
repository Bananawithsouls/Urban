def add_everything_up(a, b):
    if type(a) == str or type(b) == str:
        # Если один из аргументов - строка, возвращаем строковое представление
        return str(a) + str(b)
    else:
        # Если оба аргумента - числа, складываем
        return round(a + b, 3)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
