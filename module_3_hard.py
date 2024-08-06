def calculate_structure_sum(data):
    total_sum = 0

    for item in data:
        if isinstance(item, (int, float)):  # Проверка, является ли элемент числом
            total_sum += item
        elif isinstance(item, str):  # Проверка, является ли элемент строкой
            total_sum += len(item)
        elif isinstance(item, set):  # Если элемент - множество, рекурсивно вызываем функцию
            total_sum += calculate_structure_sum(item)
        elif isinstance(item, list):  # Если элемент - список, рекурсивно вызываем функцию
            total_sum += calculate_structure_sum(item)
        elif isinstance(item, tuple):  # Если элемент - кортеж, рекурсивно вызываем функцию
            total_sum += calculate_structure_sum(item)
        elif isinstance(item, dict):  # Если элемент - словарь, обрабатываем ключи и значения
            total_sum += calculate_structure_sum(item.keys())
            total_sum += calculate_structure_sum(item.values())

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
