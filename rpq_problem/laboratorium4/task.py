class Task:
    """
    Zadanie.
    Posiada ID oraz czasy przygotowania, wykonania i dostarczenia,
    pozwala się porównywać i konwertować do stringa, w formie "Task 1 (r=2, p=3, q=4)".
    """
    def __init__(self, task_id: int, preparation_time: int, execution_time: int, delivery_time: int) -> None:
        self._id = task_id
        self._preparation_time = preparation_time
        self._execution_time = execution_time
        self._delivery_time = delivery_time

    def get_id(self) -> int:
        return self._id

    def get_preparation_time(self) -> int:
        return self._preparation_time

    def get_execution_time(self) -> int:
        return self._execution_time

    def get_delivery_time(self) -> int:
        return self._delivery_time

    def change_preparation_time(self, preparation_time: int):
        self._preparation_time = preparation_time
        return self

    def change_execution_time(self, execution_time: int):
        self._execution_time = execution_time
        return self

    def change_delivery_time(self, delivery_time: int):
        self._delivery_time = delivery_time
        return self

    def copy(self):
        return Task(self._id, self._preparation_time, self._execution_time, self._preparation_time)

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
        return f"Task {self._id} (r={self._preparation_time}, p={self._execution_time}, q={self._delivery_time})"

    def __repr__(self) -> str:
        return f"Task {self._id}"
