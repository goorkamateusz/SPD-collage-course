from ortools.sat.python.cp_model import CpModel, CpSolver

"""
Klasa Task przechowywująca podstawowe informacje o danym zadaniu.
"""

class Task:

    id = 0
    time = 0
    penalty = 0
    deadline = 0

    def __init__(self, id, time, penalty, deadline):
        
        self.id = id
        self.time = time
        self.penalty = penalty
        self.deadline = deadline

###################################################################################

"""
Klasa WiTiProblem zajmuje się rozwiązaniem problemu Ważonych kar  zapomocą solvera ortools.
"""

class WiTiProblem:

    wt_model = CpModel()
    wt_solver = CpSolver()

    tasks = []
    tasks_nb = 0

    """
    Metoda load_from_file służy do załadowania danych z pliku.
    """

    def load_from_file(self, file_name: str):
        
        file = open(file_name, "r")
        self.tasks_nb = int(next(file))

        for id in range(0, self.tasks_nb):
            
            row = next(file).split()
            time = (int(row[0]))
            penalty = (int(row[1]))
            deadline = (int(row[2]))
            
            task = Task(id, time, penalty, deadline)
            self.tasks.append(task)

    ###################################################################################

    """
    Metoda solve uruchamia solver.
    """

    def solve(self):

        print("\nSolver włączony")
        self.wt_solver.parameters.max_time_in_seconds = 8
        self.wt_solver.Solve(self.wt_model)
        print("Solver zakończony\n")

    ###################################################################################

    """
    Metoda run jest podstawową metodą definiowania problemu.
    """

    def run(self, file_name):

        self.load_from_file(file_name)

        time_sum = 0
        for task_nbr in range(0, self.tasks_nb):
            time_sum = time_sum + self.tasks[task_nbr].time

        sum_lateness = 0
        for task_nbr in range(self.tasks_nb):
            sum_lateness += self.tasks[task_nbr].penalty * self.tasks[task_nbr].deadline

        objective_min = 0
        objective_max = sum_lateness + 1

        variable_max_value = 1 + time_sum
        variable_min_value = 0

        starts = []
        finishes = []
        intervals = []
        lates = []


        objective = self.wt_model.NewIntVar(objective_min, objective_max, "WiTi")

        for task_nbr in range(self.tasks_nb):
            
            nbr = str(task_nbr)
            start = self.wt_model.NewIntVar(variable_min_value, variable_max_value, "start" + nbr)
            finish = self.wt_model.NewIntVar(variable_min_value, variable_max_value, "finish" + nbr)
            interval = self.wt_model.NewIntervalVar(start, self.tasks[task_nbr].time, finish, "interval" + nbr)
            late = self.wt_model.NewIntVar(objective_min, objective_max, "late" + nbr)

            starts.append(start)
            finishes.append(finish)
            intervals.append(interval)
            lates.append(late)

        self.wt_model.AddNoOverlap(intervals)

        for task_nbr in range(self.tasks_nb):
            self.wt_model.Add(lates[task_nbr] >= 0)
            self.wt_model.Add(lates[task_nbr] >= (finishes[task_nbr] - self.tasks[task_nbr].deadline) * self.tasks[task_nbr].penalty)

        max_t = sum(lates)
        self.wt_model.Add(objective >= max_t)

        self.wt_model.Minimize(objective)

        self.solve()

        output_tasks_order = []
        for task_nbr in range(self.tasks_nb):
            output_tasks_order.append((task_nbr, self.wt_solver.Value(starts[task_nbr])))
        
        output_tasks_order.sort(key=lambda x: x[1])
        output_tasks_order = [x[0] for x in output_tasks_order]

        print("Suma: " + str(int(self.wt_solver.ObjectiveValue())))
        print("Kolejność zadań: " + str(output_tasks_order))