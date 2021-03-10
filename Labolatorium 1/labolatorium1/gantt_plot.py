import matplotlib.pyplot as plt
from labolatorium1.general_lib import Machine, Task

class GanttPlot():
    colors = ["red", "blue", "yellow", "green", "orange"]

    def __init__(self, machines: list[Machine]):
        self.__machines = machines
        _, self.gnt = plt.subplots()
        self._set_limit()
        self._set_labels()
        self._set_ticks()
        self._draw_plot()

    def show(self):
        plt.show()

    def _draw_plot(self):
        self.gnt.grid(True)

        # todo
        self.gnt.broken_barh([(40, 50)], (30, 9), facecolors =('tab:orange'))
        self.gnt.broken_barh([(110, 10), (150, 10)], (10, 9), facecolors ='tab:blue')
        self.gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9), facecolors =('tab:red'))
        # todo

    def _set_limit(self):
        self.gnt.set_ylim(0, len(self.__machines))
        self.gnt.set_xlim(0, self._get_c_max())

    def _set_labels(self):
        self.gnt.set_xlabel("Time")
        self.gnt.set_ylabel("Machines")

    def _set_ticks(self):
        self.gnt.set_yticks([15, 25, 35])
        self.gnt.set_yticklabels(['1', '2', '3'])

    def _get_c_max(self):
        return 16
        # todo
