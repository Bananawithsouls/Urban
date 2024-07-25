# 1st program"
result = (9 ** 0.5) * 5
print(result)
# 2nd program
result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)
# 3rd program
num1 = 1234
num2 = 5678
# Извлечение серединных чисел
middle1 = (num1 // 10) % 100
middle2 = (num2 // 10) % 100
# Сумма серединных чисел
result = middle1 + middle2
print(result)  # Ожидаемый результат: 90
# 4th program
num1 = 13.42
num2 = 42.13
# Проверка целой части одного числа на равенство дробной части другого
result = (int(num1) == int(num2 * 100) % 100) or (int(num2) == int(num1 * 100) % 100)
print(result)


