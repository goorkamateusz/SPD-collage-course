#!/usr/bin/python3
from laboratorium4.Cmax_calculator import CMaxCalculator
from laboratorium4.rpq_task_reader import RpqTaskReader
from laboratorium4.schrage_algorithm import SchrageAlgorithm
from laboratorium4.schrage_n_log_n import SchrageNLogNAlgorithm


if __name__ == "__main__":
    c_max_calculator = CMaxCalculator()

    print('SCHRAGE')
    tasks = RpqTaskReader.read('example_data/in200.txt')
    result = SchrageAlgorithm().run(tasks)
    c_max = c_max_calculator.get_Cmax(result)
    print('C MAX', c_max)

    print('SCHRAGE n log n')
    tasks = RpqTaskReader.read('example_data/in200.txt')
    result = SchrageNLogNAlgorithm().run(tasks)
    c_max = c_max_calculator.get_Cmax(result)
    print('C MAX', c_max)
