from typing import List, Tuple
import collections
from ortools.sat.python.cp_model import CpModel, CpSolver

class JSProblem:

    js_model = CpModel()
    js_solver = CpSolver()

    tasks_nb = 0
    machines_nb = 0
    operations_nb = 0

    def load_from_file(self, file_name: str):

        file = open(file_name, "r")
        
        self.tasks_nb, self.machines_nb, self.operations_nb = [int(x) for x in next(file).split()]
        
        jobshop_data = []
        for task in range(0, self.tasks_nb):

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

    def solve(self):

        self.js_solver.parameters.max_time_in_seconds = 8
        self.js_solver.Solve(self.js_model)

    ###################################################################################

    def print_result(self, jobshop_matrix, all_tasks, machines):

        # Printowanie
        assigned_task_type = collections.namedtuple('assigned_task_type','start job index')
        assigned_jobs = collections.defaultdict(list)
        for job_id, job in enumerate(jobshop_matrix):
            for task_id, task in enumerate(job):
                machine = task[0]
                assigned_jobs[machine].append(
                    assigned_task_type(start=self.js_solver.Value(all_tasks[job_id, task_id].start),
                        job=job_id, index=task_id,))

        output = ''
        for machine in range(1, machines+1):
            assigned_jobs[machine].sort() # kazde zadanie sortujemy zeby dostac je w kolejnosci rozpoczynania sie
            line_to_print = 'Machine ' + str(machine) + ': '

            for assigned_task in assigned_jobs[machine]:
                name = assigned_task.job*machines+assigned_task.index+1
                # Add spaces to output to align columns.
                line_to_print += '%i ' % name

            output += line_to_print + '\n'

        print('Cmax: %i' % self.js_solver.ObjectiveValue())
        print(output)

    ###################################################################################

    def run(self, filename):
        
        jobshop_data = self.load_from_file(filename)

        task_type = collections.namedtuple('task_type', 'start end interval')

        all_tasks = {}
        machine_to_intervals = collections.defaultdict(list)
        worst_possibly_cmax = sum(task[1] for job in jobshop_data for task in job) # maksymalny czas trwania danego zadania (gorne ograniczenie) - jest to najgorszy mozliwy do uzyskania czas

        for job_id, job in enumerate(jobshop_data):
            for task_id, task in enumerate(job):
                machine = task[0]
                duration = task[1]

                start_var = self.js_model.NewIntVar(0, worst_possibly_cmax, 'start' ) # tworzenie zmiennych z ograniczeniami (0 - max czas trwania), zmienne calkowitoliczbowe
                end_var = self.js_model.NewIntVar(0, worst_possibly_cmax, 'end')

                interval_var = self.js_model.NewIntervalVar(start_var, duration, end_var, 'interval') # interwal - start, czas trwania, koniec

                all_tasks[job_id, task_id] = task_type(start=start_var, end=end_var, interval=interval_var)
                machine_to_intervals[machine].append(interval_var)

        for machine in range(1, self.machines_nb +1):
            self.js_model.AddNoOverlap(machine_to_intervals[machine])  # ograniczenie na nachodzenie sie zadan tylko na danej maszynie

        for job_id, job in enumerate(jobshop_data):
            for task_id in range(len(job) - 1):
                self.js_model.Add(all_tasks[job_id, task_id + 1].start >= all_tasks[job_id, task_id].end)
                # operacje musza sie rozpoczynac po zakonczeniu poprzednich


        cmax_var = self.js_model.NewIntVar(0, worst_possibly_cmax, 'cmax')
        self.js_model.AddMaxEquality(cmax_var,
                            [all_tasks[job_id, len(job) - 1].end for job_id, job in enumerate(jobshop_data)])
        self.js_model.Minimize(cmax_var) # szukamy najszbyszego zakonczenia zadan

        self.solve()

        self.print_result(jobshop_data, all_tasks, self.machines_nb)