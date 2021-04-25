from typing import List

from laboratorium4.task import Task


class Algorithm:
    """
    Klasa abstrakcyjna dla wszystkich algorytmów

    Wszystkie algorytmy powinny zaimplementować funkcję run(), która przyjmuje listę zadań
    i zwraca listę zadań w wyznaczonej kolejności.
    """
    name = NotImplemented

    def run(self, tasks: List[Task]) -> List[Task]:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.name

    def __eq__(self, oth) -> bool:
        return str(self) == str(oth)
