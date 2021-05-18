import sys
import getopt
from typing import List
from laboratorium4.Cmax_calculator import CMaxCalculator

from laboratorium4.algorithm import Algorithm
from laboratorium4.rpq_task_reader import RpqTaskReader
from laboratorium4.schrage_algorithm import SchrageAlgorithm
from laboratorium4.schrage_n_log_n import SchrageNLogNAlgorithm
from laboratorium4.schrage_pmtn import SchragePMTNAlgorithm
from laboratorium4.schrage_pmtn_n_log_n import SchragePMTNNLogNAlgorithm
from laboratorium4.schrage_pmtn_sorted_list import SchragePMTNSortedListAlgorithm
from laboratorium4.time_profiler import TimeProfiler
from laboratorium4.generate_plot import GeneratePlot

from laboratorium5.calier_algorithm import CalierAlgorithm


class UIManager:
    filenames = []
    _algorithm = []
    _print_result = False

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
        Option("f:", "file=", "śceżka do pliku"),
        Option("d:", "dir=", "ścieżka do katalogu"),
        Option("h", "help", ""),
        Option("r", "result", "wyświetl resultat"),
    ]

    @staticmethod
    def default_alg():
        UIManager._add_alg(SchrageAlgorithm())
        #UIManager._add_alg(SchrageNLogNAlgorithm())
        #UIManager._add_alg(SchragePMTNAlgorithm())
        #UIManager._add_alg(SchragePMTNNLogNAlgorithm())
        #UIManager._add_alg(SchragePMTNSortedListAlgorithm())
        UIManager._add_alg(CalierAlgorithm())

    @staticmethod
    def algorithms() -> List[Algorithm]:
        return UIManager.algorithms

    @staticmethod
    def load_sys_arg():
        arg_list = sys.argv[1:]
        options = "".join([opt.short for opt in UIManager._options])
        long_options = [opt.long for opt in UIManager._options]

        try:
            args, _ = getopt.getopt(arg_list, options, long_options)
            for curr_arg, curr_val in args:
                if curr_arg in ("-f", "--file"):
                    UIManager.filenames.append(curr_val)

                if curr_arg in ("-d", "--dir"):
                    for filename in RpqTaskReader.all_in_dir(curr_val):
                        UIManager.filenames.append(filename)

                if curr_arg in ("-r", "--result"):
                    UIManager._print_result = True

                if curr_arg in ("-h", "--help"):
                    UIManager.help()
                    exit()

        except getopt.error as err:
            print(str(err))
            exit()

        if UIManager.filenames is None:
            print("Nie podano nazwy pliku wejsciowego")
            exit()

        if not UIManager._algorithm:
            print("Nie wybrano algorytmu")

    @staticmethod
    def print(result, algorithm: Algorithm, profiler: TimeProfiler) -> None:
        if isinstance(result, list):
            c_max_calculator = CMaxCalculator()
            c_max = c_max_calculator.get_Cmax(result)
        else:
            c_max = result

        print(algorithm.name)
        print(f"| C_max = {c_max}")
        print(f"| Czas obliczeń = {profiler}")
        if UIManager._print_result:
            print(f"| Resultat:\n{result}")
        print("")

    @staticmethod
    def help() -> None:
        for op in UIManager._options:
            print(op)

    @staticmethod
    def _add_alg(alg: Algorithm) -> None:
        if alg not in UIManager._algorithm:
            UIManager._algorithm.append(alg)
