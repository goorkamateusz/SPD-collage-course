import sys
import getopt
from os import walk
from typing import List
from dodatkowo.tabu_search import TabuSearchV2

from labolatorium1.silly_algorithm import SillyAlgorithm
from labolatorium1.johnson_rule import JohnsonRule
from labolatorium1.all_possibilities import AllPossibilities
from labolatorium2.NEH_algorithm import NehAlgorithm
from labolatorium2.NEH_algorithm_modification import NehAlgorithmModification
from labolatorium2.modifications import *
from labolatorium2.without_modification import WithoutModification
from laboratorium3.initial_solution_generator import CopyTasks, InitialSolutionGenerator, UseAlgorithm
from laboratorium3.neightbourhood_generator import Insert, Inverse, NeightbourhoodGenerator, SwapAll
from laboratorium3.stop_conditions import ComplexStopCondition, IterCondition, StopConditions, TimeCondition, WithoutProgresCondition
from laboratorium3.tabu_search import TabuSearch
from laboratorium6.ortools_flowshop import FlowshopSolver


class UIManager:
    file_names = []
    algorithm = []
    _modifications = {
        0: WithoutModification(),
        1: FirstModification(),
        2: SecondModification(),
        3: ThirdModification(),
        4: FourthModification()
    }

    class Option:
        def __init__(self, short: str, long: str, description: str):
            self.short = short
            self.long = long
            self.description = description

        def __str__(self) -> str:
            short = self.short.replace(":", " arg")
            long = self.long.replace("=", "=arg")
            return f"{short}\t{long}\t - {self.description}"

    _options = [
        Option("f:", "file=", "nazwa pliku"),
        Option("d:", "dir=", "ścieżka do katalogu"),
        Option("a", "all", ""),
        Option("s", "silly-alg", ""),
        Option("p", "all-permutation", ""),
        Option("j", "johnson-rule", ""),
        Option("n", "neh-algorithm", ""),
        Option("N:", "neh-algorithm-modyfications", "arg: 0, 1, 2, 3, 4"),
        Option("t:", "tabu-search", "arg - tabu list length"),
        Option("T:", "tabu-search-modyfications",
"""arg: <tabli list length>,<init>,<neighbour>,<stop>
\t\t\tinit: {c, s, j, n, N1, N2, N3, N4},
\t\t\tneighbour: {sw, in, iv}
\t\t\tstop: {i<max_iter>, t<max_time>, p<max_iter_without_progres>}"""),
        Option("Y:", "tabu-search-modyfications-v2",
"""arg: <tabli list length>,<init>,<neighbour>,<stop>
\t\t\tinit: {c, s, j, n, N1, N2, N3, N4},
\t\t\tneighbour: {sw, in, iv}
\t\t\tstop: {i<max_iter>, t<max_time>, p<max_iter_without_progres>}"""),
        Option("o", "ortools-flowshop", ""),
        Option("h", "help", ""),
    ]

    @staticmethod
    def display_and_print(machines_with_task: list, algorithm) -> None:
        # for machine in machines_with_task:
        #     print(machine)

        print(str(algorithm) + " | czas obliczeń: " + str(algorithm.bench_time_us/1000) + "ms")

        gantt = Gantt(machines_with_task)
        print(f"Czas trwania {gantt.get_duration()}")
        gantt.plot(str(algorithm))

    @staticmethod
    def show_plots():
        Gantt.Plot.show()

    @staticmethod
    def load_sys_arg():
        arg_list = sys.argv[1:]
        options = "".join([opt.short for opt in UIManager._options])
        long_options = [opt.long for opt in UIManager._options]

        try:
            args, _ = getopt.getopt(arg_list, options, long_options)
            for curr_arg, curr_val in args:
                if curr_arg in ("-f", "--file"):
                    UIManager.file_names.append(curr_val)

                if curr_arg in ("-d", "--dir"):
                    for filename in UIManager.all_in_dir(curr_val):
                        UIManager.file_names.append(filename)

                if curr_arg in ("-a", "--all"):
                    # UIManager._add_alg(SillyAlgorithm())
                    UIManager._add_alg(JohnsonRule())
                    # UIManager._add_alg(AllPossibilities())
                    UIManager._add_alg(NehAlgorithm())
                    UIManager._add_alg(TabuSearch())
                    UIManager._add_alg(FlowshopSolver())
                    # for modification in UIManager._modifications.values():
                    #     UIManager._add_alg(NehAlgorithmModification(modification))

                if curr_arg in ("-s", "--silly-alg"):
                    UIManager._add_alg(SillyAlgorithm())

                if curr_arg in ('-p', "--all-permutation"):
                    UIManager._add_alg(AllPossibilities())

                if curr_arg in ('-j', "--johnson-rule"):
                    UIManager._add_alg(JohnsonRule())

                if curr_arg in ('-n', "--neh-algorithm"):
                    UIManager._add_alg(NehAlgorithm())

                if curr_arg in "-N":
                    if "," in curr_val:
                        for val in curr_val.split(','):
                            UIManager._add_alg(NehAlgorithmModification(UIManager._modifications[int(val)]))
                    else:
                        UIManager._add_alg(NehAlgorithmModification(UIManager._modifications[int(curr_val)]))

                if curr_arg in ('-t', "--tabu-search"):
                    UIManager._add_alg(TabuSearch())

                if curr_arg in ('-T'):
                    UIManager._add_tabu_serach_with_modification(curr_val)

                if curr_arg in ('-Y'):
                    if "," in curr_val:
                        list_length, initial_switch, neighbour_switch, stop_switch = curr_val.split(",")
                        initial = UIManager._get_initial_alg(initial_switch)
                        neighbour = UIManager._get_neighbour_alg(neighbour_switch)
                        stop = UIManager._get_stop_con(stop_switch)
                        UIManager._add_alg(TabuSearchV2(int(list_length), initial, neighbour, stop))
                    else:
                        UIManager._add_alg(TabuSearchV2())

                if curr_arg in ("--tabu-list", None):
                    TabuSearch.tabu_list_max_length = int(curr_val)

                if curr_arg in ('-o', '--ortools-flowshop'):
                    UIManager._add_alg(FlowshopSolver())

                if curr_arg in ("-h", "--help"):
                    UIManager.help()
                    exit()

        except getopt.error as err:
            print(str(err))
            exit()

        if not UIManager.file_names:
            print("Nie podano nazwy pliku wejsciowego")
            exit()

        if not UIManager.algorithm:
            print("Nie wybrano algorytmu")

    @staticmethod
    def _add_alg(alg) -> None:
        if alg not in UIManager.algorithm:
            UIManager.algorithm.append(alg)

    @staticmethod
    def _add_tabu_serach_with_modification(curr_val: str) -> None:
        if "," in curr_val:
            list_length, initial_switch, neighbour_switch, stop_switch = curr_val.split(",")
            initial = UIManager._get_initial_alg(initial_switch)
            neighbour = UIManager._get_neighbour_alg(neighbour_switch)
            stop = UIManager._get_stop_con(stop_switch)
            UIManager._add_alg(TabuSearch(int(list_length), initial, neighbour, stop))
        else:
            UIManager._add_alg(TabuSearch())

    @staticmethod
    def _get_initial_alg(initial_switch: str) -> InitialSolutionGenerator:
        if "s" in initial_switch:
            return UseAlgorithm(SillyAlgorithm())
        if "j" in initial_switch:
            return UseAlgorithm(JohnsonRule())
        if "n" in initial_switch:
            return UseAlgorithm(NehAlgorithm())
        if "N" in initial_switch:
            modifaction_id = int(initial_switch.replace("N", ""))
            return UseAlgorithm(NehAlgorithmModification(UIManager._modifications[modifaction_id]))
        else:
            return CopyTasks()

    @staticmethod
    def _get_neighbour_alg(neighbour_switch: str) -> NeightbourhoodGenerator:
        if "in" in neighbour_switch:
            return Insert()
        elif "iv" in neighbour_switch:
            return Inverse()
        else:
            return SwapAll()

    @staticmethod
    def _get_stop_con(stop_switch: str) -> StopConditions:
        if "+" in stop_switch:
            return UIManager._get_complex_stop_con(stop_switch)
        elif "i" in stop_switch:
            max_iter = int(stop_switch.replace("i", ""))
            return IterCondition(max_iter)
        elif "t" in stop_switch:
            max_time = float(stop_switch.replace("t", ""))
            return TimeCondition(max_time)
        elif "p" in stop_switch:
            max_no_progres = int(stop_switch.replace("p", ""))
            return WithoutProgresCondition(max_no_progres)
        else:
            return IterCondition(10)

    @staticmethod
    def _get_complex_stop_con(stop_switch: str) -> ComplexStopCondition:
        simple_switches = stop_switch.split("+")
        conditions = []
        for switch in simple_switches:
            conditions.append(UIManager._get_stop_con(switch))
        return ComplexStopCondition(conditions)

    @staticmethod
    def help() -> None:
        for op in UIManager._options:
            print(op)

    @staticmethod
    def all_in_dir(path: str) -> List[str]:
        _, _, filenames = next(walk(path))
        return [f"{path}/{filename}" for filename in filenames]
