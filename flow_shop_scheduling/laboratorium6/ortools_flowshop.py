from itertools import combinations
from typing import List, Tuple

from ortools.sat.python import cp_model

from labolatorium1.general_lib import Machine, Task
from labolatorium2.algorithm import Algorithm


class FlowshopSolver(Algorithm):
    name = "Flowshop solver algorithm"

    def run(self, machines: List[Machine], tasks: List[Task]) -> List[Machine]:
        Cmax, pi_order, status = self.solve_flowshop_with_solver(machines, tasks)
        tasks_order = [tasks[task_index] for task_index in pi_order]
        print(Cmax, status, tasks_order)
        for task in tasks_order:
            for machine in machines:
                machine.add_task(task)
        return machines

    def solve_flowshop_with_solver(self, machines: List[Machine], tasks: List[Task]) -> Tuple[float, List[int], str]:
        model = cp_model.CpModel()
        variable_min_value = 0
        variable_max_value = 0
        for machine in machines:
            for task in tasks:
                variable_max_value += machine.get_task_duration(task)

        min_values = []
        first_row = []
        for i in range(0, len(tasks)):
            first_row.append(0)
        min_values.append(first_row)

        for machine_index in range(len(machines)-1):
            machine_row = []
            for task in tasks:
                machine_row.append(machines[machine_index].get_task_duration(task) + min_values[machine_index][task.get_id()-1])
            min_values.append(machine_row)

        max_values = []
        machine_sum = 0
        for machine_index, machine in enumerate(machines):
            for task in tasks:
                machine_sum += machine.get_task_duration(task)
            max_values.append(machine_sum)

        cmax_optimization_objective = model.NewIntVar(variable_min_value, variable_max_value, 'cmax_makespan')

        model_start_vars = []
        model_ends_vars = []

        for machine in machines:
            model_interval_vars = []
            end_vars = []
            start_vars = []
            for task in tasks:
                suffix = f"t:{task.get_id()}_{machine.get_id()}"
                start_var = model.NewIntVar(min_values[machine.get_id()-1][task.get_id()-1], variable_max_value, 'start_' + suffix)
                start_vars.append(start_var)
                end_var = model.NewIntVar(variable_min_value, max_values[machine.get_id()-1], 'end_' + suffix)
                end_vars.append(end_var)
                interval_var = model.NewIntervalVar(start_var, machine.get_task_duration(task), end_var, 'interval_' + suffix)
                model_interval_vars.append(interval_var)
            model_ends_vars.append(end_vars)
            model_start_vars.append(start_vars)
            model.AddNoOverlap(model_interval_vars)

        for end_var in model_ends_vars[-1]:
            model.Add(cmax_optimization_objective >= end_var)

        for i in range(len(machines)-1):
            for j in range(len(tasks)):
                model.Add(model_start_vars[i+1][j] >= model_ends_vars[i][j])

        for i in range(len(machines)-1):
            for first_index, second_index in combinations(range(len(tasks)), 2):
                suffix = f"t:{machine.get_id()}_{first_index}_{second_index}"
                is_first_greater_than_second = model.NewBoolVar('is_positive' + suffix)
                model.Add((model_start_vars[i][second_index] - model_start_vars[i][first_index]) >= -max_values[i]*(1-is_first_greater_than_second))
                model.Add((model_start_vars[i+1][second_index] - model_start_vars[i+1][first_index]) >= -max_values[i+1]*(1-is_first_greater_than_second))
                model.Add((model_start_vars[i][second_index] - model_start_vars[i][first_index]) <= max_values[i]*is_first_greater_than_second)
                model.Add((model_start_vars[i+1][second_index] - model_start_vars[i+1][first_index]) <= max_values[i+1]*is_first_greater_than_second)

        model.Minimize(cmax_optimization_objective)

        solver = cp_model.CpSolver()
        # solver.parameters.max_time_in_seconds = 60.0
        status = solver.Solve(model)

        if status is not cp_model.OPTIMAL:
            status_readable = "no optimal solution found :("
        else:
            status_readable = "optimum found!"

        pi_order = sorted(range(len(tasks)), key=lambda task_number: solver.Value(model_start_vars[0][task_number]))

        return solver.ObjectiveValue(), pi_order, status_readable
