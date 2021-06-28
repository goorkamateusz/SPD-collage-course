#!/usr/bin/python3
import random

examples_nb = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
max_t = 2000

for nb in examples_nb:

    file = open("../example_data/rand/rand." + str(nb), "w")

    file.writelines(str(nb) + "\n")

    line = ""
    for i in range(0, nb):
        line = str(random.randint(0, max_t)) + " " + str(random.randint(0, max_t)) + " " + str(random.randint(0, max_t)) + "\n"
        file.writelines(line)

    file.close()
    