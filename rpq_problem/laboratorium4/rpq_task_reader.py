from itertools import count
from typing import List
from os import walk

from laboratorium4.task import Task


class RpqTaskReader:
    """
    Odczytuje plik o podanej ścieżce i zwraca listę zadań do wykonania.
    Obecnie działa jedynie dla plików in50.txt, in100.txt i in200.txt.
    """
    @staticmethod
    def read(path: str, ifRand = False) -> List[Task]:

        with open(path, 'r') as file:
            tasks = []
            lines = file.readlines()
            tasks_number = int(lines[0].split()[0])

            for i in range(1, tasks_number+1):
                r, p, q = lines[i].split()
                task = Task(i, int(r), int(p), int(q))
                tasks.append(task)

            return tasks

    @staticmethod
    def all_in_dir(path: str) -> List[str]:
        _, _, filenames = next(walk(path))
        return [f"{path}/{filename}" for filename in filenames]