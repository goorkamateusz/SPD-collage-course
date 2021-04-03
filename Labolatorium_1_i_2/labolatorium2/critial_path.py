from labolatorium1.calculable_lib import TaskAssigned

from typing import List


class CritialPath:
    def __init__(self):
        self._dictionary = {}
        self._critical_path = []
        self._modified = True

    def add(self, task: TaskAssigned) -> None:
        if task.finish in self._dictionary:
            self._dictionary[task.finish].append(task)
        else:
            self._dictionary[task.finish] = [task]
        self._modified = True

    def get_path(self) -> List[TaskAssigned]:
        if self._modified:
            self._calculate()
        return self._critical_path

    def _calculate(self) -> None:
        task = self._get_last_task()
        self._critical_path.insert(0, task)

        while task.start > 0:
            task = self._get_task_before(task)
            self._critical_path.insert(0, task)

        self._modified = False

    def _get_last_task(self) -> TaskAssigned:
        finish_time = max(self._dictionary.keys())
        return self._dictionary[finish_time][0]

    def _get_task_before(self, task: TaskAssigned) -> TaskAssigned:
        for t in self._dictionary[task.start]:
            if t == task:
                return t

        for t in self._dictionary[task.start]:
            if t.machine_id == task.machine_id:
                return t

        raise Exception("Mysle ze to jest nie mozliwe")
