from labolatorium1.general_lib import *


class JohnsonRule:

    def task_w_min_duration(self, machines: list, tasks: list) -> Task:

        """ Wyszukiwanie i usuwanie najkrótszego zadania
        Parameters
        ----------
        machines : list
            Lista maszyn z ustawionymi czasami zadań;
        tasks : list
            Lista zadań;

        Returns
        -------
        task
            Zadanie z najkrótszym czasem wykonywania (niezależnie od maszyny);
        """

        # Szukanie taska z najkrótszym czasem
        tmpTsk = tasks[0]
        min = 9999
        for task in tasks:
            for machine in machines:
                if machine.get_task_duration(task) < min:
                    min = machine.get_task_duration(task)
                    tmpTsk = task


        # Usuwanie znalezionego taska
        for task in tasks:
            if task is tmpTsk:
                tasks.remove(task)
        
        return tmpTsk

    def run(self, machines: list, tasks: list) -> list:
        """ Algorytm Johnsona

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

        beginInd = 0
        endInd = len(tasks)

        newTasks = [None] * endInd

        while beginInd < endInd:
            
            minTask = self.task_w_min_duration(machines, tasks)

            machineA = machines[0]

            if machineA.has_task(minTask):
                newTasks[beginInd] = minTask
                beginInd += 1
            else:
                newTasks[endInd - 1] = minTask
                endInd -= 1


        for task in newTasks:
            for machine in machines:
                machine.add_task(task)

        return machines