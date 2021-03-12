
class Task:
    def __init__(self, id: int) -> None:
        self.__id = id
        pass

    def get_id(self) -> int:
        return self.__id

    def __eq__(self, other) -> bool:
        if (other is not Task):
            return False
        else:
            return self.__id == other.__id

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __hash__(self) -> int:
        return hash(self.__id)

    def __str__(self) -> str:
        return f"Task: {self.__id}"


class Machine:
    def __init__(self, id: int) -> None:
        self.tasks = []
        self.__id = id
        self.__tasks_durations = {}
        self.time_line = None

    def get_id(self) -> int:
        return self.__id

    def has_task(self, task: Task) -> bool:
        return task in self.tasks

    def add_task(self, new_task: Task) -> None:
        self.tasks.append(new_task)

    def get_number_of_tasks(self) -> int:
        return len(self.tasks)

    def time_line_is_calculated(self) -> bool:
        return self.time_line is not None

    def add_task_duration(self, task: Task, time: int) -> None:
        self.__tasks_durations[task] = time

    def get_task_duration(self, task: Task) -> int:
        try:
            return self.__tasks_durations[task]
        except KeyError:
            raise KeyError

    def __eq__(self, other) -> bool:
        return self.__id == other.__id

    def __nq__(self, other) -> bool:
        return not (self == other)

    def __str__(self) -> str:
        out = f"Machine {self.__id}\n"
        for task in self.tasks:
            out += f"| {task} | {self.get_task_duration(task)}\n"
        return out
