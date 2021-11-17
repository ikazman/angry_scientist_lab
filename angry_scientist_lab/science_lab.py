import random
import statistics
import time

random.seed(42)  # фикисируем случайные числа


class ScienceLab:
    """Класс для имитации работы лаборатории для разведения крыс:
    https://en.wikipedia.org/wiki/Brown_rat."""

    def __init__(self, goal=50000, rats_in_lab=20, generation_limit=500):
        """Исходные параметры для генетического алгоритма для разведения
        суперкрыс из Rattus norvegicus."""
        self.goal = goal  # определяем желаемый итоговый вес крысы (в граммах)
        self.rats_in_lab = rats_in_lab  # максимум число крыс в лаборатории
        self.init_min_weight = 200
        self.init_max_weight = 600
        self.init_mode_weigth = 300
        self.mutate_odds = 0.01  # вероятность мутации особи
        self.mutate_min = 0.5  # коэффициент наименее полезной мутации
        self.mutate_max = 1.2  # коэффициент наиболее полезной мутации
        self.litter_size = 8
        self.litters_per_year = 10
        self.generation_limit = generation_limit  # число поколений

    def rats_number_even(self):
        """Проверяем, что в лаборатиории четное число крыс для разведения."""
        if self.rats_in_lab % 2 != 0:
            self.rats_in_lab += 1

    def populate(self, min_weight, max_weight, mode_weight):
        """Инициализируем популяцию крыс с помощью треугольного распределения:
        https://docs.python.org/3/library/random.html#random.triangular"""
        return [int(random.triangular(min_weight, max_weight, mode_weight))
                for _ in range(self.rats_in_lab)]
