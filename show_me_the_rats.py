import time
from angry_scientist import angry_scientist_and_minions

if __name__ == '__main__':
    start = time.time()
    angry_totally_not_mad = angry_scientist_and_minions.AngryScentist()
    angry_totally_not_mad.report()
    end = time.time()
    duration = end - start
    print(f'\nАлгоритм выполнен за {duration} сек.')