#!/usr/bin/python3

"""
Splitter plików Dr.a Makuchowskiego.
Wymaga do działania:
1. pliku: neh.data.txt
2. folderu splitted
"""

file = open("neh.data.txt", "r")
lines = file.readlines()
file.close()

print("Rozpoczynam parsowanie pliku")

for line in lines:

    if "data" in line:
        file.close()
        file = open(("splitted/" + line)[:-2], "w")
        
    else:
        file.write(line)

file.close()
print("Parsowanie zakończone")
