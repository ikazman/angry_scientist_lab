from angry_scientists_lab import science_lab


class AngryScentist:
    """Класс для проведения эксперимента и сбора результатов."""

    def __init__(self):
        """Инициализируем счетчик поколений, список для сбора статистики."""
        self.generation = 0
        self.average_weights = []

    def report(self):
        """Запускем эксперимент, собираем отчет, выводим результат."""
        lab = science_lab.ScienceLab()
        parents = lab.populate()
        print(f'Изначальные веса популяции: {parents}')
        pop_fitness = lab.fitness(parents)
        print(f'Изначальное соответствие показателей цели: {pop_fitness}')
        print(f'Максимальное число крыс в лаборатории: {lab.rats_in_lab}')

        while pop_fitness < 1 and self.generation < lab.generation_limit:
            selected_males, selected_females = lab.selection(parents)
            children = lab.breed(selected_males, selected_females)
            children = lab.mutate(children)
            parents = selected_males + selected_females + children
            pop_fitness = round(lab.fitness(parents), 2)
            print(f'Показатели поколения {self.generation}: {pop_fitness}')
            self.average_weights.append(lab.mean_statistic(parents))
            self.generation += 1
        print(f'\nСредний вес на поколение в кг: {self.average_weights}')
        print(f'\nЧисло поколений: {self.generation}')
        print(f'\nЧисло лет: {int(self.generation / lab.litters_per_year)}')
