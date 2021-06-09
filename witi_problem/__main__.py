#!/usr/bin/python3
from witi_problem import WiTiProblem
import sys

if __name__ == "__main__":

    #witi_problem = WitiProblem()
    #witi_problem.run(sys.argv[1])

    test_instance = WiTiProblem.load_from_file(sys.argv[1])
    test_instance.solve_witi_with_solver()