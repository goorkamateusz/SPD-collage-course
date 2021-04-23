#!/usr/bin/python3

"""
Splitter plików Dr.a Makuchowskiego.
Wymaga do działania:
1. pliku: schr.data.txt
2. folderu example_data

Do wywołania w folderze Mkh_splitter
"""

file = open("schr.data.txt", "r")
lines = file.readlines()
file.close()

for line in lines:

    if "data" in line:
        file.close()
        file = open(("../example_data/" + line)[:-2], "w")

    else:
        file.write(line)

file.close()
