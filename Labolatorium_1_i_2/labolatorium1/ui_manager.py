import sys
import getopt

from labolatorium1.silly_algorithm import SillyAlgorithm
from labolatorium1.johnson_rule import JohnsonRule
from labolatorium1.all_possibilities import AllPossibilities
from labolatorium1.general_lib import Task, Machine
from labolatorium1.gantt_plot import Gantt
from labolatorium2.NEH_algorithm import NehAlgorithm
from labolatorium2.NEH_algorithm_modification import NehAlgorithmModification
from labolatorium2.modifications import *
from labolatorium2.without_modification import WithoutModification


class UIManager:
    file_name = None
    algorithm = []
    _modifications = {
        0: WithoutModification(),
        1: FirstModification(),
        2: SecondModification(),
        3: ThirdModification(),
        4: FourthModification()
    }

    @staticmethod
    def display_and_print(machines_with_task: list, algorithm) -> None:
        for machine in machines_with_task:
            print(machine)

        gantt = Gantt(machines_with_task)
        print(f"Czas trwania {gantt.get_duration()}")
        gantt.plot(algorithm.name)

    @staticmethod
    def show_plots():
        Gantt.Plot.show()

    @staticmethod
    def load_sys_arg():
        arg_list = sys.argv[1:]
        options = "f:spjnm:ah"
        long_options = ["file=", "silly-alg", "all-permutation", "johnson-rule", "neh-algorithm", "all", "help"]

        try:
            args, _ = getopt.getopt(arg_list, options, long_options)
            for curr_arg, curr_val in args:
                if curr_arg in ("-f", "--file"):
                    UIManager.file_name = curr_val

                if curr_arg in ("-a", "--all"):
                    UIManager._add_alg(SillyAlgorithm())
                    UIManager._add_alg(JohnsonRule())
                    UIManager._add_alg(AllPossibilities())
                    UIManager._add_alg(NehAlgorithm())

                if curr_arg in ("-s", "--silly-alg"):
                    UIManager._add_alg(SillyAlgorithm())

                if curr_arg in ('-p', "--all-permutation"):
                    UIManager._add_alg(AllPossibilities())

                if curr_arg in ('-j', "--johnson-rule"):
                    UIManager._add_alg(JohnsonRule())

                if curr_arg in ('-n', "--neh-algorithm"):
                    UIManager._add_alg(NehAlgorithm())

                if curr_arg in ("-m"):
                    UIManager._add_alg(NehAlgorithmModification(UIManager._modifications[int(curr_val)]))

                if curr_arg in ("-h", "--help"):
                    for c in options:
                        if c != ":":
                            print(f"-{c}")
                    for l in long_options:
                        print(l)
                    exit()

        except getopt.error as err:
            print(str(err))
            exit()

        if UIManager.file_name is None:
            print("Nie podano nazwy pliku wejsciowego")
            exit()

        if not UIManager.algorithm:
            print("Nie wybrano algorytmu")

    @staticmethod
    def _add_alg(alg) -> None:
        for alg_on_list in UIManager.algorithm:
            if type(alg_on_list) == type(alg):
                return
        UIManager.algorithm.append(alg)
