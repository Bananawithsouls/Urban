import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def reset(self):
        self.distance = 0

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance  # Полная дистанция
        self.participants = list(participants)  # Список участников

    def start(self):
        finishers = {}  # Словарь для хранения финишировавших участников
        place = 1  # Место финишировавшего участника

        while self.participants:
            for participant in list(self.participants):  # Использую копию списка
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)  # Удаляем участника после финиша
        return finishers


class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()

        print({place: str(runner) for place, runner in results.items()})

        self.assertEqual(results[1].name, "Усэйн")  # Проверка, что Усэйн финишировал первым

    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()

        print({place: str(runner) for place, runner in results.items()})

        self.assertEqual(results[1].name, "Андрей")  # Проверка, что Андрей финишировал первым

    def test_race_usain_and_andrey_and_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()

        print({place: str(runner) for place, runner in results.items()})

        # Проверка порядка финиша
        expected_order = ["Усэйн", "Андрей", "Ник"]
        actual_order = [results[place].name for place in sorted(results.keys())]
