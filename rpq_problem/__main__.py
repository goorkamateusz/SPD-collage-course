#!/usr/bin/python3
from laboratorium4.Cmax_calculator import CMaxCalculator
from laboratorium4.rpq_task_reader import RpqTaskReader
from laboratorium4.time_profiler import TimeProfiler
from laboratorium4.ui_manager import UIManager


if __name__ == "__main__":
    c_max_calculator = CMaxCalculator()
    time_profiler = TimeProfiler()

    UIManager.default_alg()
    UIManager.load_sys_arg()

    tasks = RpqTaskReader.read(UIManager.file_name)

    for algorithm in UIManager._algorithm:
        tasks_copy = tasks.copy()
        time_profiler.start()
        result = algorithm.run(tasks_copy)
        time_profiler.stop()
        c_max = c_max_calculator.get_Cmax(result)
        UIManager.print(c_max, algorithm, time_profiler)
