import math
from collections import deque
from typing import List

from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import *
from labolatorium2.algorithm import Algorithm
from laboratorium3.neightbourhood_generator import NeightbourhoodGenerator, SwapAll
from laboratorium3.initial_solution_generator import InitialSolutionGenerator, CopyTasks


class TabuSearch(Algorithm):
    name = "Algorytm tabu search"

    def __init__(self,
                neigthbourhood_generator: NeightbourhoodGenerator = SwapAll(),
                intial_solution_generator: InitialSolutionGenerator = CopyTasks()) -> None:
        super().__init__()
        self.intial_solution_generator = intial_solution_generator
        self.neigthbourhood_generator = neigthbourhood_generator

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
        initial_solution = self.intial_solution_generator.run(tasks)

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
            neighbors = self.neigthbourhood_generator.run(current_neighborhood_best_solution)
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
