#!/usr/bin/python3
def print_comb2():
    for i in range(100):
        if i < 99:
            print(f"{i:02}", end=", ")
        else:
            print(f"{i:02}")
