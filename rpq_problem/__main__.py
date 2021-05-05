#!/usr/bin/python3
from laboratorium4.rpq_task_reader import RpqTaskReader
from laboratorium4.time_profiler import TimeProfiler
from laboratorium4.ui_manager import UIManager
from laboratorium4.generate_plot import GeneratePlot

if __name__ == "__main__":
    time_profiler = TimeProfiler()

    UIManager.default_alg()
    UIManager.load_sys_arg()

    for filename in UIManager.filenames:
        print(f"--- {filename} ---")
        tasks = RpqTaskReader.read(filename)

        for algorithm in UIManager._algorithm:

            tasks_copy = tasks.copy()
            time_profiler.start()
            result = algorithm.run(tasks_copy)
            time_profiler.stop()            
            
            UIManager.print(result, algorithm, time_profiler)
            GeneratePlot.add_data(result, algorithm, time_profiler, len(tasks))

    GeneratePlot()