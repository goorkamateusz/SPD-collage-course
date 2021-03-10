
class Task:
    def __init__(self, id: int) -> None:
        self.__id = id
        pass

    def get_id(self) -> int:
        return self.__id

    def __eq__(self, other) -> bool:
        return self.__id == other.__id

    def __ne__(self, other) -> bool:
        return self.__id != other.__id

    def __hash__(self) -> int:
        return self.__id


class Machine:
    def __init__(self, id: int) -> None:
        self.tasks = []
        self.__id = id
        self.__tasks_durations = {}

    def get_id(self) -> int:
        return self.__id

    def get_duration(self) -> int:
        sum = 0
        for task in self.tasks:
            sum = sum + self.get_task_duration(task)
        return sum

    def get_number_of_tasks(self) -> int:
        return len(self.tasks)

    def add_task_duration(self, task: Task, time: int) -> None:
        self.__tasks_durations[task] = time

    def get_task_duration(self, task: Task) -> int:
        try:
            return self.__tasks_durations[task]
        except KeyError:
            raise KeyError

    def add_task(self, new_task: Task) -> None:
        self.tasks.append(new_task)

    def __eq__(self, other: Task) -> bool:
        return self.__id == other.__id
