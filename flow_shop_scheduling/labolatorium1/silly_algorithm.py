from typing import List

from labolatorium1.general_lib import *
from labolatorium2.algorithm import Algorithm


class SillyAlgorithm(Algorithm):
    name = "Bezmyślny algorytm"

    def run(self, machines: List[Machine], tasks: List[Task]) -> List[Machine]:
        """ Dodaje zadania pokoleii do maszyn

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

        for task in tasks:
            for machine in machines:
                machine.add_task(task)

        return machines
