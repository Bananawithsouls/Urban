import unittest


# Определение класса Runner
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


# Определение класса Tournament
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)

    return wrapper


# Определение класса RunnerTest
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Измените на True, чтобы заморозить тесты

    @skip_if_frozen
    def test_challenge(self):
        runner = Runner("Usain Bolt")
        runner.run()
        self.assertEqual(runner.distance, 10)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Marathon Runner")
        runner.run()
        self.assertEqual(runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Walker")
        runner.walk()
        self.assertEqual(runner.distance, 5)


# Определение класса TournamentTest
class TournamentTest(unittest.TestCase):
    is_frozen = True  # Измените на False, чтобы разблокировать тесты

    @skip_if_frozen
    def test_first_tournament(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        tournament = Tournament(15, runner1, runner2)
        finishers = tournament.start()
        self.assertIn(1, finishers)

    @skip_if_frozen
    def test_second_tournament(self):
        runner1 = Runner("Runner A")
        runner2 = Runner("Runner B")
        tournament = Tournament(20, runner1, runner2)
        finishers = tournament.start()
        self.assertIn(1, finishers)

    @skip_if_frozen
    def test_third_tournament(self):
        runner1 = Runner("Runner X")
        runner2 = Runner("Runner Y")
        tournament = Tournament(25, runner1, runner2)
        finishers = tournament.start()
        self.assertIn(1, finishers)


if __name__ == '__main__':
    unittest.main()
