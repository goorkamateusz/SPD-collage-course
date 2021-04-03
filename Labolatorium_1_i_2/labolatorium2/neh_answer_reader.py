from labolatorium1.file_manager import FileManager

from typing import List
from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Machine

class FileWithoutAnswer(Exception):
    pass


class NehFileReader(FileManager):

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file = NehFileReader._open_file(file_name)

    def data(self):
        return NehFileReader.read_data(self.file)

    def answer(self):
        self._find_answer_header()
        duration = int(self.file.readline())
        tasks_order = self._get_task_order()
        return (duration, tasks_order)

    def verify_algorithm(self, alg):
        (machines, tasks) = self.data()
        machines_with_task_order = alg.run(machines, tasks)
        self.assert_answer(machines_with_task_order)

    def assert_answer(self, machines: List[Machine]):
        gantt = Gantt(machines)
        first_machne = machines[0]
        actual_order = [task.get_id() for task in first_machne.tasks]
        expected_duration, expected_order = self.answer()

        try:
            assert gantt.get_duration() == expected_duration, f"Task duration is not equal\nexpected: {expected_duration}, actual: {gantt.get_duration()}\nfile: {self.file_name}"
            assert actual_order == expected_order, f"Task order is not equal,\nexcpected:\n{expected_order}\nactual:\n{actual_order}\nfile: {self.file_name}"
        except Exception as ex:
            gantt.plot(self.file_name)
            Gantt.Plot.show()
            raise ex

    def _find_answer_header(self) -> None:
        while True:
            line = self.file.readline()
            if line == "neh:\n":
                break
            elif line == None:
                raise FileWithoutAnswer()

    def _get_task_order(self) -> List[int]:
        task_order = []
        for line in self.file.readlines():
            if line != "\n":
                numbers = list(map(int, line[0:-1].split(" ")))
                task_order.extend(numbers)
        return task_order
