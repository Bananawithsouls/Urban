def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Вызов функции inner_function внутри test_function


# Вызов test_function
test_function()

# Вызов inner_function вне test_function
inner_function()  # Это вызывает ошибку, потому что inner_function не доступна
