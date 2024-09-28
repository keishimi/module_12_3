import unittest
from runner_and_tournament import Tournament
from runner_and_tournament import Runner
import tests_12_2

from unittest import TextTestRunner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        print("Настройка класса RunnerTest")

    @classmethod
    def tearDownClass(cls):
        print("Очистка класса RunnerTest")

    def test_challenge(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка вызова метода challenge")

    def test_run(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка вызова метода run")

    def test_walk(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка вызова метода walk")

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        print("Настройка класса TournamentTest")

    @classmethod
    def tearDownClass(cls):
        print("Очистка класса TournamentTest")

    def test_first_tournament(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка первого турнира")

    def test_second_tournament(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка второго турнира")

    def test_third_tournament(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка третьего турнира")

# Создаем TestSuite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Запускаем TestSuite с TextTestRunner
runner = TextTestRunner(verbosity=2)
result = runner.run(suite)

# Вывод результатов тестов
print(result)