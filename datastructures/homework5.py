# Создание переменных разных типов данных
immutable_var = (1, 2, 'a', 'b')
# Вывод кортежа immutable_var
print("Immutable tuple:", immutable_var)
# Изменение значений переменных
# Попытка изменить элементы кортежа immutable_var
#print(type(immutable_var))
#  попытка изменить элемент кортежа, например:
#       immutable_var[2] = 8
#  выдаст ошибку, кортеж не поддерживает обращение по элементам
#print('Tuple does not support element-by-element handling\n')
# Создание изменяемых структур данных
mutable_list = [1, 2, 'a', 'b']
# Изменение элементов списка mutable_list
mutable_list.append('Modified')
# Вывод измененного списка mutable_list
print("Mutable list:", mutable_list)
