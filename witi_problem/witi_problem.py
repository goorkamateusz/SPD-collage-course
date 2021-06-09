
"""
class WitiProblem:

    pass
"""


class WiTi_Task:
    def __init__(self, task_number, p, w, t):
        self.id: int = task_number
        self.p: int = p
        self.t: int = t
        self.w: int = w

    def __repr__(self):
        return "[i:{0},p:{1},w:{2},t:{3}]".format(self.id, self.p, self.w, self.t)


class WiTiProblem:

    tasks: list
    tasks_number: int

    @staticmethod
    def load_from_file(file_path: str):
        instance = WiTiProblem()
        try:
            with open(file_path, "r") as file:
                next(file)
                row = next(file).split()
                instance.tasks_number = int(row[0])
                instance.tasks = []

                for i in range(0, instance.tasks_number):
                    row = next(file).split()
                    p = (int(row[0]))
                    w = (int(row[1]))
                    t = (int(row[2]))
                    task = WiTi_Task(i, p, w, t)
                    instance.tasks.append(task)

        except FileNotFoundError:
            print("File not found.")
            raise FileNotFoundError

        return instance

    def print_instance(self):
        print(self.tasks)
        print('Tasks:', self.tasks_number)

    def get_p(self, task_number):
        return self.tasks[task_number].p

    def get_w(self, task_number):
        return self.tasks[task_number].w

    def get_t(self, task_number):
        return self.tasks[task_number].t

def solve_witi_with_solver(instance: WiTiProblem):
    from ortools.sat.python import cp_model
    model = cp_model.CpModel()

    sum_p = 0
    for task_number in range(instance.tasks_number):
        sum_p = sum_p + instance.get_p(task_number)

    sum_lateness = 0
    for task_number in range(instance.tasks_number):
        sum_lateness = instance.get_w(task_number) * instance.get_t(task_number)

    objective_min = 0
    objective_max = sum_lateness + 1

    variable_max_value = 1 + sum_p
    variable_min_value = 0

    model_start_vars = []
    model_ends_vars = []
    model_interval_vars = []
    model_late_vars = []


    objective = model.NewIntVar(objective_min, objective_max, 'Witi objective')

    for task_number in range(instance.tasks_number):
        suffix = f"t:{task_number}"
        start_var = model.NewIntVar(variable_min_value, variable_max_value, 'start_' + suffix)
        end_var = model.NewIntVar(variable_min_value, variable_max_value, 'end_' + suffix)
        interval_var = model.NewIntervalVar(start_var, instance.get_p(task_number), end_var, 'interval_' + suffix)
        late_var = model.NewIntVar(objective_min, objective_max, 'late_' + suffix)

        model_start_vars.append(start_var)
        model_ends_vars.append(end_var)
        model_interval_vars.append(interval_var)
        model_late_vars.append(late_var)

    model.AddNoOverlap(model_interval_vars)

    for task_number in range(instance.tasks_number):
        model.Add(model_late_vars[task_number] >= 0)
        model.Add(model_late_vars[task_number] >= (model_ends_vars[task_number] - instance.get_t(task_number)) * instance.get_w(task_number))

    max_t = sum(model_late_vars)
    model.Add(objective >= max_t)

    model.Minimize(objective)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 300.0

    status = solver.Solve(model)

    if (status is not cp_model.OPTIMAL):
        status_readable = "not optimal solution :( -- nie wiem dlaczego, wyniki sa optymalne a solver mówi że nie"
    else:
        status_readable = "optimum found!"


    pi_order = []
    for task_number in range(instance.tasks_number):
        pi_order.append((task_number, solver.Value(model_start_vars[task_number])))
    pi_order.sort(key=lambda x: x[1])
    pi_order = [x[0] for x in
                pi_order]

    return solver.ObjectiveValue(), pi_order, status_readable