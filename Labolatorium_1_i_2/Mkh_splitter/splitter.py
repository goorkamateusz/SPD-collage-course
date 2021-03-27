#!/usr/bin/python3

file = open("neh.data.txt", "r")
context = file.readlines()
file.close()

for line in lines:

    if "data" in line:
        file.close()
        file = open("splitted/" + line, "w")