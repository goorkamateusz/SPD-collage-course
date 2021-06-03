from typing import List, Tuple

from ortools.sat.python import cp_model

from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task


class RpqInstance:
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks
        self.tasks_number = len(tasks)

    def get_r(self, task_number: int) -> int:
        return self.tasks[task_number].get_preparation_time()

    def get_p(self, task_number: int) -> int:
        return self.tasks[task_number].get_execution_time()

    def get_q(self, task_number: int) -> int:
        return self.tasks[task_number].get_delivery_time()


class RpqSolver(Algorithm):
    name = 'RPQ solver algorithm'
    id = 10

    def run(self, tasks: List[Task]) -> List[Task]:
        rpq_instance = RpqInstance(tasks)
        Cmax, pi_order, status = self.solve_rpq_with_solver(rpq_instance)
        print(Cmax, status)
        tasks_order = [tasks[task_index] for task_index in pi_order]
        return tasks_order

    def solve_rpq_with_solver(self, instance: RpqInstance) -> Tuple[float, List[int], str]:
        model = cp_model.CpModel()

        max_r = 0
        max_q = 0
        sum_p = 0
        for task_number in range(instance.tasks_number):
            sum_p = sum_p + instance.get_p(task_number)
            max_r = max(max_r, instance.get_r(task_number))
            max_q = max(max_q, instance.get_q(task_number))

        variable_max_value = 1 + max_r + sum_p + max_q
        variable_min_value = 0

        model_start_vars = []
        model_ends_vars = []
        model_interval_vars = []

        cmax_optimalization_objective = model.NewIntVar(variable_min_value, variable_max_value, 'cmax_makespan')

        for task_number in range(instance.tasks_number):
            suffix = f"t:{task_number}"
            start_var = model.NewIntVar(variable_min_value, variable_max_value, 'start_' + suffix)
            end_var = model.NewIntVar(variable_min_value, variable_max_value, 'end_' + suffix)
            interval_var = model.NewIntervalVar(start_var, instance.get_p(task_number), end_var, 'interval_' + suffix)

            model_start_vars.append(start_var)
            model_ends_vars.append(end_var)
            model_interval_vars.append(interval_var)

        model.AddNoOverlap(model_interval_vars)

        for task_number in range(instance.tasks_number):
            model.Add(model_start_vars[task_number] >= instance.get_r(task_number))

        for task_number in range(instance.tasks_number):
            model.Add(cmax_optimalization_objective >= model_ends_vars[task_number] + instance.get_q(task_number))

        model.Minimize(cmax_optimalization_objective)

        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = 300.0
        status = solver.Solve(model)

        if status is not cp_model.OPTIMAL:
            status_readable = "no optimal solution found :("
        else:
            status_readable = "optimum found!"

        pi_order = sorted(range(instance.tasks_number),
                          key=lambda task_number: solver.Value(model_start_vars[task_number]))
        return solver.ObjectiveValue(), pi_order, status_readable
