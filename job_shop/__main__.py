#!/usr/bin/python3
from job_shop import JSProblem
import sys

if __name__ == "__main__":

    js_problem = JSProblem()
    js_problem.run(sys.argv[1])