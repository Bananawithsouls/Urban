# Входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Преобразовываем множество студентов в отсортированный список
sorted_students = sorted(students)
# Создаем словарь с именами студентов и их средними баллами
# Использую enumerate для получения индексов студентов и соответствующие им списки оценок
average_grades = {
    student: sum(grades[i]) / len(grades[i])
    for i, student in enumerate(sorted_students)
}
print(average_grades)