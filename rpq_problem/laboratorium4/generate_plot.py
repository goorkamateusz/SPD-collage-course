import sys
import matplotlib.pyplot as plt

from laboratorium4.Cmax_calculator import CMaxCalculator

class GeneratePlot:

    Schrage_data = []
    SchrageNLogN_data = []
    SchragePMTN_data = []
    SchragePMTNNLogN_data = []
    SchragePMTNSortedList_data = []

    @staticmethod
    def add_data(result, added_algorithm, time_profiler, task_number):

        if isinstance(result, list):
            c_max_calculator = CMaxCalculator()
            c_max = c_max_calculator.get_Cmax(result)
        else:
            c_max = result

        data = [task_number, c_max, int(str(time_profiler))]

        if added_algorithm.id == 0:
            GeneratePlot.Schrage_data.append(data)

        elif added_algorithm.id == 1:
            GeneratePlot.SchrageNLogN_data.append(data)

        elif added_algorithm.id == 2:
            GeneratePlot.SchragePMTN_data.append(data)

        elif added_algorithm.id == 3:
            GeneratePlot.SchragePMTNNLogN_data.append(data)

        elif added_algorithm.id == 4:
            GeneratePlot.SchragePMTNSortedList_data.append(data)

        else:
            raise ValueError
        

    def __init__(self):
        
        fig1, ax1 = plt.subplots()
        

        ax1.plot(self.Schrage_data[0],               self.Schrage_data[1],               label="Schrage")
        ax1.plot(self.SchrageNLogN_data[0],          self.SchrageNLogN_data[1],          label="Schrage nlogn")
        ax1.plot(self.SchragePMTN_data[0],           self.SchragePMTN_data[1],           label="Schrage z przerywaniem")
        ax1.plot(self.SchragePMTNNLogN_data[0],      self.SchragePMTNNLogN_data[1],      label="Schrage z przerywaniem nlogn")
        ax1.plot(self.SchragePMTNSortedList_data[0], self.SchragePMTNSortedList_data[1], label="Schrage z przerywaniem lista sortowana")
                
        ax1.legend()

        plt.show()
        
