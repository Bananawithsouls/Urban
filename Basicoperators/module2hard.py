def generate_password(n):
    result = ""

    # Генерируем уникальные пары
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            numbers_sum = i + j

            # Проверяем кратность
            if n % numbers_sum == 0:
                result += f"{i}{j}"

    return result

# Ввод числа от 3 до 20
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")

