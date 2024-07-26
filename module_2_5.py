def get_matrix(n, m, value):  # Объявляем функцию get_matrix и записываем в ней параметры n, m и value
    # Создаем пустой список для матрицы
    matrix = []
    # Проверяем, чтобы n и m были больше 0
    if n <= 0 or m <= 0:
        return matrix  # Возвращаем пустой список
    # Внешний цикл для количества строк
    for _ in range(n):
        # Создаем пустой список для строки
        row = []
        # Внутренний цикл для количества столбцов
        for _ in range(m):
            row.append(value)  # Добавляем значение в строку
        matrix.append(row)  # Добавляем строку в матрицу
    return matrix  # Возвращаем заполненную матрицу


# Пример использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
# Выводим результаты на консоль
print(result1)
print(result2)
print(result3)
