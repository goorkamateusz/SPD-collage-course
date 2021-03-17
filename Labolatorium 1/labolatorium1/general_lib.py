class Task:
    """
    Zadanie.
    Posiada ID, pozwala się porównywać i konwertować do stringa, w formie "Task 1".
    """
    def __init__(self, id: int) -> None:
        self._id = id

    def get_id(self) -> int:
        return self._id

    def __eq__(self, other) -> bool:
        if isinstance(other, Task):
            return self._id == other._id
        else:
            return False

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __hash__(self) -> int:
        return hash(self._id)

    def __str__(self) -> str:
        return f"Task {self._id}"

    def __repr__(self) -> str:
        return f"{self._id}"


class Machine:
    """
    Maszyna.
    - `add_task_duration(task, time)` i odpowiednio `get_task_duration(task)`
      obsługują czas trwania wykonywanie zadań na maszynie i muszą być zainicjowane;
    - Posiada listę `tasks` do zapisywania kolejności wykonywanych zadań na maszynie:
      `has_task(task)`, `add_task(task)`;
    - Jest porównywalna i konwertuje się do stringa w formie, np:
      "Machine 1
      | Task1 | 10
      | Task2 | 12"
    """
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

    def clear_tasks(self) -> None:
        self.tasks.clear()

    def get_number_of_tasks(self) -> int:
        return len(self.tasks)

    def add_task_duration(self, task: Task, time: int) -> None:
        self._tasks_durations[task] = time

    def get_task_duration(self, task: Task) -> int:
        try:
            return self._tasks_durations[task]
        except KeyError as error:
            raise error

    def __eq__(self, other) -> bool:
        if isinstance(other, Machine):
            return self._id == other._id
        else:
            return False

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __str__(self) -> str:
        out = f"Machine {self._id}\n"
        for task in self.tasks:
            out += f"| {task} | {self.get_task_duration(task)}\n"
        return out
