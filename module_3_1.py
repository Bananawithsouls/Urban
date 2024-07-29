calls = 0  # Глобальная переменная для подсчета вызовов функций


# Увеличивает значение переменной calls на 1 каждый раз при вызове
def count_calls():
    global calls
    calls += 1


# Принимает строку, вызывает count_calls, затем возвращает кортеж с длиной строки, строкой в верхнем и нижнем регистре
def string_info(string):
    count_calls()  # Увеличивает счетчик вызовов
    length = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    return length, upper_string, lower_string


# Принимает строку и список, вызывает count_calls, проверяет наличие строки в списке без учета регистра
def is_contains(string, list_to_search):
    count_calls()  # Увеличивает счетчик вызовов
    string_lower = string.lower()  # Приводим искомую строку к нижнему регистру
    return any(item.lower() == string_lower for item in
               list_to_search)  # Проверяем наличие строки в списке,приводя каждый элемент списка к нижнему регистру


# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

# Выводим общее количество вызовов
print(calls)
