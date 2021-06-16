#!/usr/bin/python3
from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task, Machine
from labolatorium1.file_manager import FileManager
from labolatorium1.ui_manager import UIManager
from laboratorium6.generate_plot import GeneratePlot

if __name__ == "__main__":

    UIManager.load_sys_arg()
    generate_plot = GeneratePlot()
    for file_name in UIManager.file_names:
        machines, tasks = FileManager.load_data(file_name)

        for algorithm in UIManager.algorithm:

            machines_copy = [m.copy_without_task_queue() for m in machines]
            tasks_copy = tasks.copy()

            algorithm.read_start_time()
            machines_with_task = algorithm.run(machines_copy, tasks_copy)
            algorithm.read_end_time()
            generate_plot.add_data(machines_with_task, algorithm, len(tasks))

            UIManager.display_and_print(machines_with_task, algorithm)
    # generate_plot.show_plot()
    UIManager.show_plots()
