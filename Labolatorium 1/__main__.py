from labolatorium1.all_possibilities import AllPossibilities
from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task, Machine
from labolatorium1.silly_algorithm import SillyAlgorithm
from labolatorium1.johnson_rule import JohnsonRule
from labolatorium1.file_manager import FileManager

import getopt, sys

def display_and_print_out(Machines: list) -> None:
    for machine in machines_with_task:
        print(machine)

    gantt = Gantt(machines_with_task)
    print(f"Czas trwania {gantt.get_duration()}")
    gantt.plot()

def get_input_file_name() -> str:
    arg_list = sys.argv[1:]
    options = "f:"
    long_options = ["--file"]

    try:
        args, _ = getopt.getopt(arg_list, options, long_options)

        for curr_arg, curr_val in args:
            if curr_arg in ("-f", "--file"):
                return curr_val

    except getopt.error as err:
        print(str(err))

    raise Exception("Nie podano nazwy pliku wejsciowego")


if __name__ == "__main__":

    try:
        file_name = get_input_file_name()
        print(f"Wczytano plik {file_name}")
    except Exception as err:
        print(str(err))
        exit()

    machines, tasks = FileManager.load_data(file_name)

    # permutacja
    algorithm = AllPossibilities()
    copy = [m.copy_without_task_queue() for m in machines]
    machines_with_task = algorithm.run(copy, tasks)
    display_and_print_out(machines_with_task)

    # algorytm Johnsona
    algorithm = JohnsonRule()
    copy = [m.copy_without_task_queue() for m in machines]
    machines_with_task = algorithm.run(copy, tasks)
    display_and_print_out(machines_with_task)
