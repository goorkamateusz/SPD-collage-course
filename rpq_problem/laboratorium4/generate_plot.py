import sys
import matplotlib as mp

from laboratorium4.ui_manager import UIManager

class GeneratePlot:

    group_names = []
    plot_data = []

    def add_group_names(self, names):
        self.group_names.append(names)

    def add_data(self, data):
        self.plot_data.append(data)