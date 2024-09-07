import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в виде кортежа

    def get_all_words(self):
        all_words = {}  # Создаём пустой словарь для хранения слов из файлов

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()  # Считываем содержимое файла и приводим к нижнему регистру
                    # Убираем пунктуацию
                    text = text.translate(str.maketrans('', '', string.punctuation + '-'))
                    words = text.split()  # Разбиваем текст на слова
                    all_words[file_name] = words  # Записываем в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        results = {}  # Словарь для хранения результатов поиска

        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1  # Находим позицию первого вхождения (счёт с 1)
                results[file_name] = position

        return results

    def count(self, word):
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        results = {}  # Словарь для хранения количества вхождений

        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            count = words.count(word)  # Считаем количество вхождений слова
            if count > 0:
                results[file_name] = count

        return results


# Пример использования класса
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Получаем все слова из файлов
print(finder2.find('TEXT'))  # Ищем позицию слова 'TEXT'
print(finder2.count('teXT'))  # Считаем количество слов 'teXT' в файлах
