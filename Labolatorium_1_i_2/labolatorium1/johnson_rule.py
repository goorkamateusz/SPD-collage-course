from typing import List

from labolatorium1.johnson_virtual import *
from labolatorium1.general_lib import *
from labolatorium2.algorithm import Algorithm


class JohnsonRule(Algorithm):
    name = "Algorytm Johnsona"

    def run(self, machines: List[Machine], tasks: List[Task]) -> List[Machine]:
        """ Algorytm Johnsona - funkcja przygotowawcza

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
        johnsonV = JohnsonVirtual()

        if len(machines) < 2:
            print("Blad - za malo maszyn")
            raise ValueError

        # Dla 2 maszyn:
        if len(machines) == 2:
            newTasks = johnsonV.jonson_2_Machines(machines[0], machines[1], tasks)

        # Dla więcej niż 2 maszyn - tworzenie maszyn wirtualnych:
        else:
            vMachineA = Machine(-1)
            vMachineB = Machine(-2)

            for task in tasks:
                middle = int(len(machines)/2)
                if len(machines) % 2:
                    middle += 1

                time = 0
                for i in range(0, middle):
                    time += machines[i].get_task_duration(task)
                vMachineA.add_task_duration(task, time)

                time = 0
                for i in range(int(len(machines)/2), len(machines)):
                    time += machines[i].get_task_duration(task)
                vMachineB.add_task_duration(task, time)

            newTasks = johnsonV.jonson_2_Machines(vMachineA, vMachineB, tasks)

        # Finalne przydzielanie zadań do maszyn:
        for task in newTasks:
            for machine in machines:
                machine.add_task(task)

        return machines