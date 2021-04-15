import itertools
from typing import List, Iterator

from labolatorium1.general_lib import *

Solution = List[Task]


class NeightbourhoodGenerator:
    name = ""
    
    def run(self, current_solution: Solution) -> Iterator[Solution]:
        raise NotImplementedError()


class SwapAll(NeightbourhoodGenerator):
    name = "Swap"

    def run(self, solution: Solution) -> Iterator[Solution]:
        for first_index, second_index in itertools.combinations(range(len(solution)), 2):
            solution_copy = solution.copy()
            solution_copy[first_index], solution_copy[second_index] = solution_copy[second_index], solution_copy[first_index]
            yield solution_copy


class Insert(NeightbourhoodGenerator):
    name = "Insert"

    def run(self, solution: Solution) -> Iterator[Solution]:
        raise NotImplementedError()


class Inverse(NeightbourhoodGenerator):
    name = "Inverse"

    def run(self, solution: Solution) -> Iterator[Solution]:
        raise NotImplementedError()
