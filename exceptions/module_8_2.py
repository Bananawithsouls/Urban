def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            # Приводим символ к числу
            result += item
        except (TypeError, ValueError):
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if not isinstance(numbers, (str, list, tuple)):
            raise TypeError

        total_sum, incorrect_data = personal_sum(numbers)

        # Обработка деления на ноль
        valid_count = len(numbers) - incorrect_data
        if valid_count == 0:
            return 0

        return total_sum / valid_count

    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Примеры
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
