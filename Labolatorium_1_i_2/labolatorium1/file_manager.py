from labolatorium1.general_lib import Machine, Task

from io import FileIO
from typing import List


class FileManager:

    @staticmethod
    def load_data(file_name: str):
        file = FileManager._open_file(file_name)
        return FileManager.read_data(file)

    @staticmethod
    def read_data(file_handler: FileIO):
        machines_num, tasks_num = FileManager._load_header(file_handler)
        machines, tasks = FileManager._load_machines_with_tasks(file_handler, machines_num, tasks_num)
        return (machines, tasks)

    @staticmethod
    def _open_file(file_name: str) -> FileIO:
        try:
            return open(file_name, 'r')
        except:
            print(f"Błąd otwierania pliku: {file_name}")
            exit()

    @staticmethod
    def _load_header(file: FileIO):
        line = file.readline().split(' ')
        return (int(line[1]), int(line[0]))

    @staticmethod
    def _load_machines_with_tasks(file: FileIO, machines_num: int, tasks_num: int):
        machines = FileManager._create_machine_list(machines_num)
        tasks = FileManager._create_task_list(tasks_num)

        for t in range(tasks_num):
            line = file.readline()
            time_on_machine = list(map(int, line.split(' ')))

            for m in range(machines_num):
                machines[m].add_task_duration(tasks[t], time_on_machine[m])

        return (machines, tasks)

    @staticmethod
    def _create_machine_list(machine_num: int) -> List[Machine]:
        return [Machine(i+1) for i in range(machine_num)]

    @staticmethod
    def _create_task_list(task_num: int) -> List[Task]:
        return [Task(i+1) for i in range(task_num)]
