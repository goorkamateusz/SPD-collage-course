from labolatorium1.johnson_virtual import *

class JohnsonRule:

    def run(self, machines: list, tasks: list) -> list:
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

        if len(machines) == 2:

            newTasks = johnsonV.jonson_2_Machines(machines[0], machines[1], tasks)

        elif len(machines) % 2:
            
            newTasks = tasks

        else:
            
            newTasks = tasks




        for task in newTasks:
            for machine in machines:
                machine.add_task(task)

        return machines