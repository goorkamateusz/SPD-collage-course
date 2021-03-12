
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

class TaskTime:
    """
    Klasa przechowujaca czas wykonania i czas trwania taska
    """
    def __init__(self, task: Task, start: int, duration: int) -> None:
        self.task = task
        self.start = start
        self.duration = duration
        self.finish = start+duration

    def get_id(self) -> int:
        return self.task.get_id()

class AllTaskAreCalculated(Exception):
    pass

class Machine:
    def __init__(self, id: int) -> None:
        self.tasks = []
        self.__id = id
        self.__tasks_durations = {}
        self.time_line = []

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

    def get_time_line_finish(self) -> int:
        if len(self.time_line) == 0:
            return 0
        else:
            return self.time_line[-1].finish

    def get_first_not_calculated_task(self) -> Task:
        if len(self.tasks) == len(self.time_line):
            raise AllTaskAreCalculated()
        return self.tasks[len(self.time_line)]

    def add_task_to_time_line(self, task: Task, start_time: int) -> None:
        duration = self.get_task_duration(task)
        self.time_line.append(TaskTime(task, start_time, duration))


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
