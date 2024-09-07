# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Определение результата соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Форматирование строк с использованием %
# 1. Количество участников первой команды
result1 = "В команде Мастера кода участников: %d !" % team1_num
print(result1)

# 2. Количество участников в обеих командах
result2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(result2)

# Форматирование строк с использованием format()
# 3. Количество задач, решённых командой 2
result3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(result3)

# 4. Время, за которое команда 2 решила задачи
result4 = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(result4)

# Форматирование строк с использованием f-строк
# 5. Количество решённых задач по командам
result5 = f"Команды решили {score_1} и {score_2} задач."
print(result5)

# 6. Исход соревнования
result6 = f"Результат битвы: {challenge_result}"
print(result6)

# 7. Количество задач и среднее время решения
result7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"
print(result7)
