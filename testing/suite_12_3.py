import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание тестового набора
test_suite = unittest.TestSuite()

# Добавление тестов в тестовый набор
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

# Запуск тестов с verbosity=2
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
