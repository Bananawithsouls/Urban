import matplotlib.pyplot as plt

# Линейный график
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y, marker='o')
plt.title('Линейный график')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

# Столбчатая диаграмма
categories = ['A', 'B', 'C']
values = [5, 7, 3]
plt.bar(categories, values)
plt.title('Столбчатая диаграмма')
plt.ylabel('Values')
plt.show()

# Круговая диаграмма
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Круговая диаграмма')
plt.axis('equal')  # Чтобы круг являлся кругом
plt.show()
