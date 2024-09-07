import math


class Figure:
    sides_count = 0  # Количество сторон фигуры (по умолчанию 0)

    def __init__(self, color, *sides):
        self._sides = []  # Инициализация списка сторон
        self._color = list(color)  # Преобразование цвета в список
        self.filled = False  # Флаг, указывающий заполнена ли фигура

        # Проверка на количество сторон и установка их
        if len(sides) == self.sides_count:
            self.set_sides(*sides)
        else:
            self._sides = [1] * self.sides_count  # Заполнение единицами, если количество сторон не совпадает

    def get_color(self):
        return self._color  # Возвращает цвет фигуры

    def __is_valid_color(self, r, g, b):
        # Проверка на корректность цвета (значения от 0 до 255)
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and \
            0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        # Установка цвета, если он валиден
        if self.__is_valid_color(r, g, b):
            self._color = [r, g, b]

    def is_valid_sides(self, *new_sides):
        # Проверка на валидность сторон (положительные целые числа и правильное количество)
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self._sides  # Возвращает длины сторон

    def __len__(self):
        return sum(self._sides)  # Возвращает периметр (сумму длин сторон)

    def set_sides(self, *new_sides):
        # Установка новых сторон, если они валидны
        if self.is_valid_sides(*new_sides):
            self._sides = list(new_sides)  # Сохранение новых длин сторон


class Circle(Figure):
    sides_count = 1  # У круга одна сторона (в данном контексте - длина окружности)

    def __init__(self, color, circumference):
        super().__init__(color, circumference)  # Вызов конструктора родительского класса
        self.__radius = circumference / (2 * math.pi)  # Вычисление радиуса на основе длины окружности

    def get_square(self):
        return math.pi * (self.__radius ** 2)  # Возвращает площадь круга


class Triangle(Figure):
    sides_count = 3  # У треугольника три стороны

    def __init__(self, color, *sides):
        super().init(color, *sides)  # Вызов конструктора родительского класса

    def get_square(self):
        a, b, c = self._sides  # Длины сторон
        p = (a + b + c) / 2  # Полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))  # Площадь треугольника по формуле Герона


class Cube(Figure):
    sides_count = 12  # У куба двенадцать рёбер

    def __init__(self, color, side_length, *sides):
        super().__init__(color, *sides)  # Вызов конструктора родительского класса
        if len(sides) == 0:
            self._sides = [side_length] * self.sides_count  # Установка всех рёбер одинаковой длиной

    def get_volume(self):
        return self._sides[0] ** 3  # Объём куба


# Проверка создания фигур
circle1 = Circle((200, 200, 100), 10)  # Создание круга с цветом и длиной окружности
cube1 = Cube((222, 35, 130), 6)  # Создание куба с цветом и длиной ребра

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменение цвета круга
print(circle1.get_color())  # Вывод нового цвета круга: [55, 66, 77]
cube1.set_color(300, 70, 15)  # Попытка установить недопустимый цвет для куба
print(cube1.get_color())  # Цвет куба остаётся прежним: [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Попытка изменить стороны куба (не изменится)
print(cube1.get_sides())  # Длины рёбер куба остаются прежними: [6, 6, ..., 6]
circle1.set_sides(15)  # Изменение радиуса круга
print(circle1.get_sides())  # Новый радиус круга: [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Вывод периметра круга: 15

# Проверка объёма (куба):
print(cube1.get_volume())  # Вывод объёма куба: 216
