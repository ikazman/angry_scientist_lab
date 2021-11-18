import random
import statistics

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

    def populate(self):
        """Инициализируем популяцию крыс с помощью треугольного распределения:
        https://docs.python.org/3/library/random.html#random.triangular"""
        return [int(random.triangular(self.init_min_weight,
                                      self.init_max_weight,
                                      self.init_mode_weigth))
                for _ in range(self.rats_in_lab)]

    def fitness(self, population):
        """Оцениваем текущее соответствие показателей популяции цели."""
        average = statistics.mean(population)
        return average / self.goal

    def selection(self, population):
        """Отбираем из популяции необходимое число особей."""
        sorted_population = sorted(population, reverse=True)
        to_retain_by_sex = self.rats_in_lab // 2
        members_by_sex = len(sorted_population // 2)
        males = sorted_population[members_by_sex:]
        females = sorted_population[:members_by_sex]
        selected_females = females[to_retain_by_sex:]
        selected_males = males[to_retain_by_sex:]
        return selected_males, selected_females

    def breed(self, males, females):
        """Размножаем крыс и получаем новое поколение."""
        children = []
        random.shuffle(males)
        random.shuffle(females)
        for male, female in zip(males, females):
            for _ in range(self.litter_size):
                child = random.randint(female, male)
                children.append(child)
        return children

    def mutate(self, children):
        """Изменяем вес родившихся крыс за счет случайных мутаций."""
        for index, rat in enumerate(children):
            if self.mutate_odds >= random.random():
                children[index] = round(
                    rat * random.uniform(self.mutate_min, self.mutate_max)
                )
        return children

    def mean_statistic(self, population):
        """Вычисляем средний вес популяции."""
        return int(statistics.mean(population))
