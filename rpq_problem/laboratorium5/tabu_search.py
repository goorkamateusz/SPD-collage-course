import math
from collections import deque
from typing import List
from laboratorium4.Cmax_calculator import CMaxCalculator

from laboratorium4.task import *
from laboratorium4.algorithm import Algorithm
from laboratorium5.stop_conditions import StopConditions, IterCondition
from laboratorium5.neightbourhood_generator import NeightbourhoodGenerator, SwapAll
from laboratorium5.initial_solution_generator import InitialSolutionGenerator, CopyTasks


class TabuSearch(Algorithm):
    name = "Algorytm tabu search"
    id = 7

    def __init__(self,
                tabu_list_max_length: int = 10,
                initial_solution_generator: InitialSolutionGenerator = CopyTasks(),
                neigthbourhood_generator: NeightbourhoodGenerator = SwapAll(),
                stop_condition: StopConditions = IterCondition(10)) -> None:
        super().__init__()
        self.intial_solution_generator = initial_solution_generator
        self.neigthbourhood_generator = neigthbourhood_generator
        self.stop_condition = stop_condition
        self.tabu_list_max_length = tabu_list_max_length
        self.name = f"{TabuSearch.name} ({tabu_list_max_length}, {initial_solution_generator.name}, {neigthbourhood_generator.name}, {stop_condition})"

    def run(self, tasks: List[Task]) -> List[Task]:
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

        initial_Cmax = CMaxCalculator().get_Cmax(tasks)

        best_solution = initial_solution.copy()
        best_Cmax = initial_Cmax
        current_neighborhood_best_solution = initial_solution.copy()

        # Inicjalizacja warunku stopu
        self.stop_condition.start()

        # Lista tabu jako kolejka FIFO
        tabu_list = deque(maxlen=self.tabu_list_max_length)

        while True:
            # Generowanie sąsiedztwa
            neighbors = self.neigthbourhood_generator.run(current_neighborhood_best_solution)
            current_neighborhood_best_Cmax = math.inf

            for current_solution in neighbors:
                current_Cmax = CMaxCalculator().get_Cmax(current_solution)

                if current_Cmax < current_neighborhood_best_Cmax and current_solution not in tabu_list:
                    current_neighborhood_best_Cmax = current_Cmax
                    current_neighborhood_best_solution = current_solution
                    tabu_list.append(current_solution)

            if current_neighborhood_best_Cmax < best_Cmax:
                best_Cmax = current_neighborhood_best_Cmax
                best_solution = current_neighborhood_best_solution

            if self.stop_condition.stop(current_Cmax):
                break

        print(best_solution, best_Cmax)

        return best_solution
