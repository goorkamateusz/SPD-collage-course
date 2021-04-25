from typing import Any, Callable, Generic, Iterable, TypeVar


T = TypeVar('T')


def identity(x: T) -> T:
    return x


class PriorityQueue(Generic[T]):
    """
    Kolejka priorytetyowa oparta na kopcu przechowująca dane dowolnego typu.
    Domyślnie typu Max, jeżeli poda się reverse=True, to kolejka jest typu Min.
    Gdy chce się porównywać elementy przy użyciu wybranego klucza, można go podać argumentem key.
    """
    def __init__(self, data: Iterable[T] = (), key: Callable = identity, reverse: bool = False) -> None:
        self._data = []
        self._is_greater = lambda first, second: (key(first) > key(second) if not reverse else key(first) < key(second))
        self._insert_many(data)

    def insert(self, element: T) -> None:
        self._data.append(element)

        index = len(self._data) - 1
        while index > 0 and self._is_greater(self._data[index], self._data[self._parent_index(index)]):
            parent_index = self._parent_index(index)
            self._data[index], self._data[parent_index] = self._data[parent_index], self._data[index]
            index = parent_index

    def top(self) -> T:
        if self.empty():
            raise RuntimeError('Kolejka jest pusta')
        return self._data[0]

    def extract(self) -> T:
        if self.empty():
            raise RuntimeError('Kolejka jest pusta')

        if len(self) == 1:
            return self._data.pop()

        root = self._data[0]
        last_element = self._data.pop()
        self._data[0] = last_element
        self._heapify(0)
        return root

    def empty(self) -> bool:
        return not bool(self)

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return len(self) > 0

    def __str__(self) -> str:
        return f'PriorityQueue({self._data})'

    def _insert_many(self, data: Iterable[T]) -> None:
        for element in data:
            self.insert(element)

    def _heapify(self, index: int) -> None:
        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)
        greatest_elem_index = index

        if left_index < len(self) and self._is_greater(self._data[left_index], self._data[index]):
            greatest_elem_index = left_index

        if right_index < len(self) and self._is_greater(self._data[right_index], self._data[greatest_elem_index]):
            greatest_elem_index = right_index

        if greatest_elem_index != index:
            self._data[greatest_elem_index], self._data[index] = self._data[index], self._data[greatest_elem_index]
            self._heapify(greatest_elem_index)

    def _parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def _right_child_index(self, index: int) -> int:
        return 2 * index + 2
