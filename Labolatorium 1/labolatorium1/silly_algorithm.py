from labolatorium1.general_lib import *

class SillyAlgorithm:
    def run(self, machines: list, tasks: list) -> list:
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
