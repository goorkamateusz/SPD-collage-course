from typing import Callable, Generic, Iterable, TypeVar


T = TypeVar('T')


def identity(x: T) -> T:
    return x


class SortedList(Generic[T]):
    def __init__(self, data: Iterable[T] = (), key: Callable = identity, reverse: bool = False) -> None:
        self._data = []
        self._key = key
        self._reverse = not reverse
        self._insert_many(data)

    def insert(self, element: T) -> None:
        self._data.append(element)
        self._sort()

    def top(self) -> T:
        return self._data[0]

    def extract(self) -> T:
        return self._data.pop(0)

    def empty(self) -> bool:
        return not bool(self)

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return len(self) > 0

    def __str__(self) -> str:
        return f'SortedList({self._data})'

    def _sort(self) -> None:
        self._data.sort(key=self._key, reverse=self._reverse)

    def _insert_many(self, data: Iterable[T]) -> None:
        for element in data:
            self.insert(element)
