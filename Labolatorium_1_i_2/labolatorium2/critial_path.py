from labolatorium1.calculable_lib import TaskTime

from typing import List


class CritialPath:
    def __init__(self):
        self.dictionary = {}
        self.critical_path = []

    def add(self, task: TaskTime) -> None:
        if task.finish in self.dictionary:
            self.dictionary[task.finish].append(task)
        else:
            self.dictionary[task.finish] = [task]

    def get_path(self) -> List[TaskTime]:
        task = self.get_last_task()
        self.critical_path.insert(0, task)

        while task.start > 0:
            task = self.get_task_before(task)
            self.critical_path.insert(0, task)

        return self.critical_path

    def get_last_task(self) -> TaskTime:
        finish_time = max(self.dictionary.keys())
        return self.dictionary[finish_time][0]

    def get_task_before(self, task: TaskTime) -> TaskTime:
        for t in self.dictionary[task.start]:
            if t == task:
                return t

        for t in self.dictionary[task.start]:
            if t.machine_id == task.machine_id:
                return t

        raise Exception("Mysle ze to jest nie mozliwe")
