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
        
        for first_index, second_index in itertools.combinations(range(len(solution)), 2):
            
            solution_copy = solution.copy()
            temp = solution_copy[first_index]

            if first_index < second_index:
                tmp_index = first_index
                first_index = second_index
                second_index = tmp_index
            
            for i in range(first_index, second_index - 1):
                solution_copy[i] = solution_copy[i + 1]

            solution_copy[second_index] = temp
            
            yield solution_copy


class Inverse(NeightbourhoodGenerator):
    name = "Inverse"

    def swapRecursive(self, first_index, second_index, solution_copy: Solution):

        if first_index >= second_index:
            return

        temp = solution_copy[first_index]
        solution_copy[first_index] = solution_copy[second_index]
        solution_copy[second_index] = temp
        
        self.swapRecursive(first_index + 1, second_index - 1, solution_copy)

    def run(self, solution: Solution) -> Iterator[Solution]:
        
        for first_index, second_index in itertools.combinations(range(len(solution)), 2):
            
            solution_copy = solution.copy()

            if first_index < second_index:
                tmp_index = first_index
                first_index = second_index
                second_index = tmp_index
            
            self.swapRecursive(first_index, second_index, solution_copy)

            yield solution_copy