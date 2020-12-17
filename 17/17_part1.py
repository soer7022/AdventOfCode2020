import sys

with open("input.txt") as f:
    data = f.read().split("\n")

neighbors_to_check = []


def check_loc(location, is_active):
    active_neighbors = 0
    x, y, z = location
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                if not a == b == c == 0:
                    if is_active:
                        neighbors_to_check.append((x + a, y + b, z + c))
                    try:
                        if active[(x + a, y + b, z + c)] is True:
                            active_neighbors += 1
                    except KeyError:
                        continue
    try:
        if active[location]:
            if not 2 <= active_neighbors <= 3:
                return False
            else:
                return True
        elif not active[location]:
            raise KeyError
    except KeyError:
        if active_neighbors == 3:
            return True
        else:
            return False


# Formatted: (x,y,z) or (col,row,layer)
active = dict()
for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == "#":
            active[(col, row, 0)] = True
for i in range(6):
    active_copy = dict(active)
    for loc in active.keys():
        active_copy[loc] = check_loc(loc, is_active=True)
    while len(neighbors_to_check) > 0:
        to_check = neighbors_to_check.pop()
        active_copy[to_check] = check_loc(to_check, is_active=False)

    active = active_copy

print(list(active.values()).count(True))
