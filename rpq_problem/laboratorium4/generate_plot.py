import sys
import matplotlib.pyplot as plt

from laboratorium4.Cmax_calculator import CMaxCalculator

class GeneratePlot:

    algorithm_data = []

    @staticmethod
    def add_data(result, algorithm, time_profiler, task_number):

        if isinstance(result, list):
            c_max_calculator = CMaxCalculator()
            c_max = c_max_calculator.get_Cmax(result)
        else:
            c_max = result

        data = [algorithm, task_number, c_max, int(str(time_profiler))]

        GeneratePlot.algorithm_data.append(data)


    def __init__(self):
        
        # C_max:
        fig1, ax1 = plt.subplots()

        for i in range(0, 6):
            x = []
            y = []
            alg_name = ""
            for sub_list in self.algorithm_data:
                if sub_list[0].id == i:
                    x.append(sub_list[1])
                    y.append(sub_list[2])
                    alg_name = sub_list[0]

            x.sort()
            y.sort()
            ax1.plot(x, y, "-", label = alg_name, alpha=0.7)
        
        plt.title("Wykres zależności C_max od ilości zadań")
        plt.xlabel("Ilość zadań")
        plt.ylabel("C_max")
        plt.grid()
        ax1.legend()

        # Czas liczenia:
        fig2, ax2 = plt.subplots()

        for i in range(0, 6):
            x = []
            y = []
            alg_name = ""
            for sub_list in self.algorithm_data:
                if sub_list[0].id == i:
                    x.append(sub_list[1])
                    y.append(sub_list[3])
                    alg_name = sub_list[0]

            x.sort()
            y.sort()
            ax2.plot(x, y, "-", label = alg_name, alpha=0.7)
        
        plt.title("Wykres zależności czasu liczenia od ilości zadań")
        plt.xlabel("Ilość zadań")
        plt.ylabel("Czas liczenia [us]")
        plt.grid()
        ax2.legend()

        plt.show()
        