class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук, который издаёт лошадь

    def run(self, dx):
        """Увеличивает пройденный путь на dx."""
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издает орел

    def fly(self, dy):
        """Увеличивает высоту полета на dy."""
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация родителя Horse
        Eagle.__init__(self)  # Инициализация родителя Eagle

    def move(self, dx, dy):
        """Перемещает пегаса по горизонтали и вертикали."""
        self.run(dx)  # Вызывает метод run из класса Horse
        self.fly(dy)  # Вызывает метод fly из класса Eagle

    def get_pos(self):
        """Возвращает текущее положение пегаса в виде кортежа (x_distance, y_distance)."""
        return self.x_distance, self.y_distance

    def voice(self):
        """Печатает звук, который издает орел."""
        print(self.sound)


# Пример работы программы
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
