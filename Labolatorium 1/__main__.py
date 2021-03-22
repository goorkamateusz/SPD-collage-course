from labolatorium1.general_lib import Task, Machine
from labolatorium1.file_manager import FileManager
from labolatorium1.ui_manager import UIManager


if __name__ == "__main__":

    UIManager.load_sys_arg()

    try:
        file_name = UIManager.file_name
        print(f"Wczytano plik {file_name}")
    except Exception as err:
        print(str(err))
        exit()

    machines, tasks = FileManager.load_data(file_name)

    for algorithm in UIManager.algorithm:
        machines_copy = [m.copy_without_task_queue() for m in machines]
        tasks_copy = tasks.copy()
        machines_with_task = algorithm.run(machines_copy, tasks_copy)
        UIManager.display_and_print(machines_with_task, algorithm)
