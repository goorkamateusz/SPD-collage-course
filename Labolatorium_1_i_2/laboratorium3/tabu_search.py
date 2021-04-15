import itertools
import math
from collections import deque
from typing import List, Iterator

from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import *
from labolatorium2.algorithm import Algorithm


Solution = List[Task]


class TabuSearch(Algorithm):
    name = "Algorytm tabu search"

    # Generowanie wszystkich możliwych sąsiadów korzystając z ruchu swap na każdej parze rozwiązania
    def swap_all(self, solution: Solution) -> Iterator[Solution]:
        for first_index, second_index in itertools.combinations(range(len(solution)), 2):
            solution_copy = solution.copy()
            solution_copy[first_index], solution_copy[second_index] = solution_copy[second_index], solution_copy[first_index]
            yield solution_copy

    def run(self, machines: List[Machine], tasks: List[Task]) -> List[Machine]:
        """ Tabu search - przeszukiwanie z zabronieniami

        Parameters
        ----------
        machines : list
            Lista maszyn z ustawionymi czasami zadań;
        tasks : list
            Lista zadań;

        Returns
        -------
        list
            Lista maszyn z dodanymi zadaniami do listy;
        """

        # Generowanie rozwiązania początkowego
        initial_solution = tasks.copy()

        for task in initial_solution:
            for machine in machines:
                machine.add_task(task)

        initial_Cmax = Gantt(machines).get_duration()

        for machine in machines:
            machine.clear_tasks()

        best_solution = initial_solution.copy()
        best_Cmax = initial_Cmax
        current_neighborhood_best_solution = initial_solution.copy()

        # Inicjalizacja warunku stopu
        iter_ = 0
        iter_max = 10

        # Lista tabu jako kolejka FIFO
        tabu_list_max_length = 10
        tabu_list = deque(maxlen=tabu_list_max_length)

        while iter_ < iter_max:
            # Generowanie sąsiedztwa
            neighbors = self.swap_all(current_neighborhood_best_solution)
            current_neighborhood_best_Cmax = math.inf
            for current_solution in neighbors:
                for task in current_solution:
                    for machine in machines:
                        machine.add_task(task)
                current_Cmax = Gantt(machines).get_duration()
                if current_Cmax < current_neighborhood_best_Cmax and current_solution not in tabu_list:
                    current_neighborhood_best_Cmax = current_Cmax
                    current_neighborhood_best_solution = current_solution
                    tabu_list.append(current_solution)
                for machine in machines:
                    machine.clear_tasks()
            if current_neighborhood_best_Cmax < best_Cmax:
                best_Cmax = current_neighborhood_best_Cmax
                best_solution = current_neighborhood_best_solution
            iter_ += 1
        print(best_solution, best_Cmax)

        for task in best_solution:
            for machine in machines:
                machine.add_task(task)
        return machines
