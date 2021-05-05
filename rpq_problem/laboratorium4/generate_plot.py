import sys
import matplotlib as mp

class GeneratePlot:

    task_numbers = []
    c_maxes = []
    algoritms = []
    times = []

    @staticmethod
    def add_task_number(task_number):
        GeneratePlot.task_numbers.append(task_number)

    @staticmethod
    def add_c_max(c_max):
        GeneratePlot.c_maxes.append(c_max)

    @staticmethod
    def add_alhorithm_and_time(algorithm, time_profiler):
        GeneratePlot.algoritms.append(str(algorithm))
        GeneratePlot.times.append(int(str(time_profiler)))

    def __init__(self):

        print("\n")
        print(self.task_numbers)
        print(self.c_maxes)
        print(self.algoritms)
        print(self.times)

        """
        fig1, ax1 = plt.subplots()
        ax1.plot(self.group_names, self.c_maxes, label="dog")
        ax1.legend()

        plt.show()
        """
