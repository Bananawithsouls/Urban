import hashlib
import time
from typing import List

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password: str) -> str:
        # Хэшируем пароль с использованием SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        # Проверяем, соответствует ли введённый пароль хэшированному
        return self.hash_password(password) == self.password

    def __str__(self):
        return f"User(nickname={self.nickname}, age={self.age})"

class Video:
        def __init__(self, title: str, duration: int, adult_mode: bool = False):
            self.title = title
            self.duration = duration  # Продолжительность в секундах
            self.time_now = 0  # Изначально 0
            self.adult_mode = adult_mode  # Ограничение по возрасту

        def play(self):
            """Начинает воспроизведение видео."""
            print(f"Воспроизведение видео '{self.title}' с {self.time_now} секунд.")

        def pause(self):
            """Приостанавливает воспроизведение видео."""
            print(f"Видео '{self.title}' приостановлено на {self.time_now} секунд.")

        def stop(self):
            """Останавливает видео и сбрасывает время."""
            print(f"Видео '{self.title}' остановлено.")
            self.time_now = 0

        def seek(self, time: int):
            """Перематывает видео на заданное время."""
            if 0 <= time <= self.duration:
                self.time_now = time
                print(f"Перемотка видео '{self.title}' на {self.time_now} секунд.")
            else:
                print("Ошибка: Время вне диапазона.")

        def __str__(self):
            return f"Video(title='{self.title}', duration={self.duration}, time_now={self.time_now}, adult_mode={self.adult_mode})"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == User.hash_password(password):
                self.current_user = user
                return
        print("Неверные логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, keyword):
        return [video.title for video in self.videos if keyword.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while video.time_now < video.duration:
                    print(video.time_now + 1)
                    video.time_now += 1
                    time.sleep(1)

                print("Конец видео")
                video.time_now = 0
                return

        print("Видео не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

