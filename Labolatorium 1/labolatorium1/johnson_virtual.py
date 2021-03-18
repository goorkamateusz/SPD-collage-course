from labolatorium1.general_lib import *

class JohnsonVirtual:

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
        min = 99999
        for task in tasks:
            for machine in machines:
                if machine.get_task_duration(task) < min:
                    min = machine.get_task_duration(task)
                    tmpTsk = task

        # Usuwanie znalezionego taska
        tasks.remove(tmpTsk)
        
        return tmpTsk

    def jonson_2_Machines(self, vMachineA, vMachineB, tasks: list) -> list:

        """ Algorytm Jonsona - problem dwumaszynowy
        Parameters
        ----------
        vMachineA
            Pierwsza maszyna wirtualna;
        vMachineB
            Druga maszyna wirtualna
        
        tasks : list
            Lista zadań;

        Returns
        -------
        list
            Lista zadań we właściwej kolejności;
        """

        beginInd = 0
        endInd = len(tasks)
        
        vMachines = [vMachineA, vMachineB]
        newTasks = [None] * endInd

        while beginInd < endInd:
            
            minTask = self.task_w_min_duration(vMachines, tasks)

            if vMachineA.get_task_duration(minTask) < vMachineB.get_task_duration(minTask):
                newTasks[beginInd] = minTask
                beginInd += 1
                
            else:
                newTasks[endInd - 1] = minTask
                endInd -= 1

        return newTasks