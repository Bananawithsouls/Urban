from random import choice

# Lambda-функция для сравнения строк
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)  # [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


# Замыкание для записи данных в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(f"{data}\n")

    return write_everything


# Пример замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Класс MysticBall с методом call
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
