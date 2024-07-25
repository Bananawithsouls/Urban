# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []
# Перебираем список numbers
for num in numbers:
    if num < 2:  # Числа меньше 2 не являются простыми
        not_primes.append(num)
        continue
    is_prime = True  # Флаг (число простое)
    # Проверяем делимость числа от 2 до корня из num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # Если num делится на i
            is_prime = False  # Число не простое
            break  # Прерываем цикл,делитель найден
    # Добавляем число в список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
# Вывод списков
print("Primes:", primes)
print("Not Primes:", not_primes)
