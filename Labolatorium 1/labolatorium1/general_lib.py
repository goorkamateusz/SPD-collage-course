
class Task:
    def __init__(self, id: int) -> None:
        self._id = id
        pass

    def get_id(self) -> int:
        return self._id

    def __eq__(self, other) -> bool:
        if (other is not Task):
            return False
        else:
            return self._id == other._id

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __hash__(self) -> int:
        return hash(self._id)

    def __str__(self) -> str:
        return f"Task: {self._id}"

class Machine:
    def __init__(self, id: int) -> None:
        self.tasks = []
        self._id = id
        self._tasks_durations = {}

    def get_id(self) -> int:
        return self._id

    def has_task(self, task: Task) -> bool:
        return task in self.tasks

    def add_task(self, new_task: Task) -> None:
        self.tasks.append(new_task)

    def get_number_of_tasks(self) -> int:
        return len(self.tasks)

    def add_task_duration(self, task: Task, time: int) -> None:
        self._tasks_durations[task] = time

    def get_task_duration(self, task: Task) -> int:
        try:
            return self._tasks_durations[task]
        except KeyError:
            raise KeyError

    def __eq__(self, other) -> bool:
        return self._id == other.__id

    def __nq__(self, other) -> bool:
        return not (self == other)

    def __str__(self) -> str:
        out = f"Machine {self._id}\n"
        for task in self.tasks:
            out += f"| {task} | {self.get_task_duration(task)}\n"
        return out
