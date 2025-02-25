#!/usr/bin/python3
def print_comb3():
    result = []
    for i in range(0, 9):
        for j in range(i + 1, 10):
            result.append(f"{i}{j}")
    print(", ".join(result)
