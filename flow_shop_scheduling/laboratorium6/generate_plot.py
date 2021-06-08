from collections import namedtuple, defaultdict

import matplotlib.pyplot as plt

from labolatorium1.gantt_plot import Gantt


AlgorithmData = namedtuple('AlgorithmData', ['algorithm', 'task_number', 'c_max', 'algorithm_duration'])


class GeneratePlot:
    def __init__(self):
        self.algorithm_data = []

    def add_data(self, machines_with_task, algorithm, task_number):
        gantt = Gantt(machines_with_task)
        c_max = gantt.get_duration()

        data = AlgorithmData(algorithm, task_number, c_max, algorithm.bench_time_us)
        print(data)
        self.algorithm_data.append(data)

    def show_plot(self):
        # C_max:
        fig1, ax1 = plt.subplots()

        algorithm_name_to_algorithm_data = defaultdict(list)
        for algorithm_data in self.algorithm_data:
            algorithm_name_to_algorithm_data[algorithm_data.algorithm.name].append(algorithm_data)

        for algorithm_name, algorithm_data_list in algorithm_name_to_algorithm_data.items():
            x_y = []
            for algorithm_data in algorithm_data_list:
                x_y.append((algorithm_data.task_number, algorithm_data.c_max))

            x_y.sort()
            x = [elem[0] for elem in x_y]
            y = [elem[1] for elem in x_y]
            ax1.plot(x, y, "-", label=algorithm_name, alpha=0.7)

        plt.title("Wykres zależności C_max od ilości zadań")
        plt.xlabel("Ilość zadań")
        plt.ylabel("C_max")
        plt.grid()
        ax1.legend()

        # Czas liczenia:
        fig2, ax2 = plt.subplots()

        for algorithm_name, algorithm_data_list in algorithm_name_to_algorithm_data.items():
            x_y = []
            for algorithm_data in algorithm_data_list:
                x_y.append((algorithm_data.task_number, algorithm_data.algorithm_duration))

            x_y.sort()
            x = [elem[0] for elem in x_y]
            y = [elem[1] for elem in x_y]
            ax2.plot(x, y, "-", label=algorithm_name, alpha=0.7)

        plt.title("Wykres zależności czasu liczenia od ilości zadań")
        plt.xlabel("Ilość zadań")
        plt.ylabel("Czas liczenia [us]")
        plt.grid()
        ax2.legend()

        plt.show()
