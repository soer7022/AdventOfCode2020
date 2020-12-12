import sys
from os import system

with open("input.txt") as f:
    data = [l.strip() for l in f.read().split("\n")]

rows = len(data)
columns = len(data[0])

prev_data = list(data)
while True:
    data_copy = list(prev_data)
    for row in range(rows):
        for column in range(columns):
            current_pos = prev_data[row][column]
            occupied = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not (i == 0 and j == 0):
                        search_row = row + i
                        search_column = column + j
                        while 0 <= search_row < rows and 0 <= search_column < columns and prev_data[search_row][search_column] == ".":
                            search_row += i
                            search_column += j
                        if 0 <= search_row < rows and 0 <= search_column < columns and prev_data[search_row][search_column] == "#":
                            occupied += 1
            if occupied == 0 and current_pos == "L":
                data_copy[row] = data_copy[row][:column] + "#" + data_copy[row][column + 1:]
            elif occupied >= 5 and current_pos == "#":
                data_copy[row] = data_copy[row][:column] + "L" + data_copy[row][column + 1:]
    equal = True
    system('clear')

    for i in range(rows):
        print(data_copy[i])
        if not data_copy[i] == prev_data[i]:
            equal = False

    if equal:
        total = 0
        for line in data_copy:
            total += line.count("#")
        print(total)
        break
    prev_data = data_copy
