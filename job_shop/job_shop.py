from typing import List, Tuple
import collections as cl
from ortools.sat.python.cp_model import CpModel, CpSolver

"""
Klasa JSProblem zajmuje się rozwiązywaniem problemu gniazdowego za pomocą solvera z ortools.
"""

class JSProblem:

    js_model = CpModel()
    js_solver = CpSolver()

    tasks_nb = 0
    machines_nb = 0
    operations_nb = 0

    """
    Metoda load_from_file służy do załadowania danych z pliku.

    """

    def load_from_file(self, file_name: str):

        file = open(file_name, "r")
        
        self.tasks_nb, self.machines_nb, self.operations_nb = [int(x) for x in next(file).split()]
        
        jobshop_data = []
        for i in range(0, self.tasks_nb):

            row = next(file).split()
            operation_in_task = int(row[0])
            single_job_data = []

            for i in range(1, operation_in_task*2, 2):
                m = int(row[i])
                p = int(row[i+1])
                single_job_data.append((m, p))
            jobshop_data.append(single_job_data)

        file.close()

        return jobshop_data

    ###################################################################################

    """
    Metoda solve uruchamia solver.
    """

    def solve(self):

        print("\nSolver włączony")
        self.js_solver.parameters.max_time_in_seconds = 8
        self.js_solver.Solve(self.js_model)
        print("Solver zakończony\n")

    ###################################################################################

    """
    Metoda print_result zajmuje się wypisaniem wyników działania solvera.
    """

    def print_result(self, jobshop_matrix, all_tasks):

        assigned_task_type = cl.namedtuple('assigned_task_type','start job index')
        assigned_jobs = cl.defaultdict(list)
        for job_id, job in enumerate(jobshop_matrix):
            for task_id, task in enumerate(job):
                machine = task[0]
                assigned_jobs[machine].append(
                    assigned_task_type(start=self.js_solver.Value(all_tasks[job_id, task_id].start),
                        job=job_id, index=task_id,))

        print("Cmax wynosi: " + str(int(self.js_solver.ObjectiveValue())))

        for machine in range(1, self.machines_nb +1):
            assigned_jobs[machine].sort()
            line_to_print = "Maszyna " + str(machine) + ': '

            for assigned_task in assigned_jobs[machine]:
                name = assigned_task.job * self.machines_nb + assigned_task.index +1
                line_to_print += str(name) + " "

            print(line_to_print)

    ###################################################################################

    """
    Metoda run jest podstawową metodą definiowania problemu.
    """

    def run(self, filename):
        
        jobshop_data = self.load_from_file(filename)

        task_type = cl.namedtuple('task_type', 'start end interval')

        all_tasks = {}
        machine_to_intervals = cl.defaultdict(list)
        worst_cmax = sum(task[1] for job in jobshop_data for task in job)

        for job_id, job in enumerate(jobshop_data):
            for task_id, task in enumerate(job):
                machine = task[0]
                duration = task[1]

                start_var = self.js_model.NewIntVar(0, worst_cmax, 'start' )
                end_var = self.js_model.NewIntVar(0, worst_cmax, 'end')

                interval_var = self.js_model.NewIntervalVar(start_var, duration, end_var, 'interval')

                all_tasks[job_id, task_id] = task_type(start=start_var, end=end_var, interval=interval_var)
                machine_to_intervals[machine].append(interval_var)

        for machine in range(1, self.machines_nb +1):
            self.js_model.AddNoOverlap(machine_to_intervals[machine])

        for job_id, job in enumerate(jobshop_data):
            for task_id in range(len(job) - 1):
                self.js_model.Add(all_tasks[job_id, task_id + 1].start >= all_tasks[job_id, task_id].end)
    

        cmax = self.js_model.NewIntVar(0, worst_cmax, 'cmax')
        self.js_model.AddMaxEquality(cmax, [all_tasks[job_id, len(job) - 1].end for job_id, job in enumerate(jobshop_data)])
        self.js_model.Minimize(cmax)

        self.solve()
        self.print_result(jobshop_data, all_tasks)