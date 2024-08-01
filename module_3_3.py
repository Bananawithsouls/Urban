def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# 1. Вызовы функции с разным количеством аргументов
print("Вызов без аргументов:")
print_params()

print("\nВызов с одним аргументом (b):")
print_params(b=25)

print("\nВызов с одним аргументом (c):")
print_params(c=[1, 2, 3])

# 2. Распаковка параметров
values_list = [1.23, 'список', False]
values_dict = {'a': 1984, 'b': 'книга', 'c': None}

print("\nРаспаковка из списка:")
print_params(*values_list)

print("\nРаспаковка из словаря:")
print_params(**values_dict)

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print("\nРаспаковка из списка + отдельный параметр:")
print_params(*values_list_2, 42)
