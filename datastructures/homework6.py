# Работа со словарями
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print("Dict:", my_dict)
# Вывод значения по существующему ключу
print("Existing value:", my_dict.get('Masha'))
# Вывод значения по отсутствующему ключу
print("Not existing value:", my_dict.get('Ivan'))
# Добавление новой пары в словарь
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915
# Удаление одной из пар и вывод удаленного значения
deleted_value = my_dict.pop('Egor')
print("Deleted value:", deleted_value)
print("Modified dictionary:", my_dict)
# Работа с множествами
my_set = {1, 'Яблоко', 42.314}  # Создание множества
print("Set:", my_set)
# Добавление элемента в множество
my_set.add(13)
my_set.add((5, 6, 1.6))
# Удаление элемента из множества
my_set.remove(1)
print("Modified set:", my_set)
