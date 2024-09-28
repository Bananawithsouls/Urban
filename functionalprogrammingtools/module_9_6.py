def all_variants(text):
    length = len(text)
    # Генерация всех последовательностей
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]


# Пример
a = all_variants("abc")
for i in a:
    print(i)
