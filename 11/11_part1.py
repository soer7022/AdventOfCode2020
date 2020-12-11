import sys

with open("input.txt") as f:
    data = f.read().split("\n")
prev_data = list(data)
while True:
    data_copy = list(prev_data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            current_pos = prev_data[i][j]
            adjacent_tiles = []
            try:
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if 0 <= k < len(data) and 0 <= l < len(data[0]) and not (k == i and j == l):
                            adjacent_tiles.append(prev_data[k][l])
            except IndexError:
                print(k,l)
                print(len(data[0]),len(prev_data[0]))
                print(len(data),len(prev_data))
                sys.exit()
            if current_pos == "L" and "#" not in adjacent_tiles:
                data_copy[i] = data_copy[i][:j] + "#" + data_copy[i][j + 1:]
            elif current_pos == "#" and adjacent_tiles.count("#") >= 4:
                data_copy[i] = data_copy[i][:j] + "L" + data_copy[i][j + 1:]
    equal = True
    for i in range(len(data_copy)):
        if not data_copy[i] == prev_data[i]:
            equal = False
    if equal:
        total = 0
        for line in data_copy:
            total += line.count("#")
        print(total)
        break
    prev_data = data_copy
