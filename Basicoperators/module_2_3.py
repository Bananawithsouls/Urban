# Исходный список
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Начальное значение индекса
index = 0
# Цикл while для перебора элементов списка
while index < len(my_list):
    number = my_list[index]  # Текущий элемент списка
    # Если встречаем отрицательное число, прерываем цикл
    if number < 0:
        break
     # Если число равно нулю, пропускаем его
    if number == 0:
        index += 1
        continue
    # Если число положительное, выводим его
    print(number)
    # Переходим к следующему элементу списка
    index += 1
