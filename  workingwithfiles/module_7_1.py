class Product:
    def __init__(self, name, weight, category):
        self.name = name  # Название продукта
        self.weight = weight  # Общий вес товара
        self.category = category  # Категория товара

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"  # Форматированный вывод


class Shop:
    __file_name = 'products.txt'  # Имя файла для хранения продуктов

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()  # Чтение всех продуктов из файла
        except FileNotFoundError:
            return ""  # Если файл не найден, возвращаем пустую строку

    def add(self, *products):
        existing_products = {line.split(', ')[0] for line in self.get_products().strip().split('\n') if line}  # Считываем существующие названия

        for product in products:
            if product.name not in existing_products:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')  # Запись нового продукта в файл
            else:
                print(f"Продукт {product.name} уже есть в магазине")  # Сообщение о существующем продукте



if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # Вывод строки продукта

    s1.add(p1, p2, p3)  # Добавление продуктов

    print(s1.get_products())  # Вывод всех продуктов из файла
