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
        for task_number in range(0, self.tasks_nb):
            time_sum = time_sum + self.tasks[task_number].time

        sum_lateness = 0
        for task_number in range(self.tasks_nb):
            sum_lateness += self.tasks[task_number].penalty * self.tasks[task_number].deadline

        objective_min = 0
        objective_max = sum_lateness + 1

        variable_max_value = 1 + time_sum
        variable_min_value = 0

        model_start_vars = []
        model_ends_vars = []
        model_interval_vars = []
        model_late_vars = []


        objective = self.wt_model.NewIntVar(objective_min, objective_max, "WiTi")

        for task_number in range(self.tasks_nb):
            
            nbr = str(task_number)
            start_var = self.wt_model.NewIntVar(variable_min_value, variable_max_value, "start" + nbr)
            end_var = self.wt_model.NewIntVar(variable_min_value, variable_max_value, "end" + nbr)
            interval_var = self.wt_model.NewIntervalVar(start_var, self.tasks[task_number].time, end_var, "interval" + nbr)
            late_var = self.wt_model.NewIntVar(objective_min, objective_max, "late" + nbr)

            model_start_vars.append(start_var)
            model_ends_vars.append(end_var)
            model_interval_vars.append(interval_var)
            model_late_vars.append(late_var)

        self.wt_model.AddNoOverlap(model_interval_vars)

        for task_number in range(self.tasks_nb):
            self.wt_model.Add(model_late_vars[task_number] >= 0)
            self.wt_model.Add(model_late_vars[task_number] >= (model_ends_vars[task_number] - self.tasks[task_number].deadline) * self.tasks[task_number].penalty)

        max_t = sum(model_late_vars)
        self.wt_model.Add(objective >= max_t)

        self.wt_model.Minimize(objective)

        self.solve()

        pi_order = []
        for task_number in range(self.tasks_nb):
            pi_order.append((task_number, self.wt_solver.Value(model_start_vars[task_number])))
        
        pi_order.sort(key=lambda x: x[1])
        pi_order = [x[0] for x in pi_order]

        print("Suma: " + str(int(self.wt_solver.ObjectiveValue())))
        print("Kolejność zadań: " + str(pi_order))