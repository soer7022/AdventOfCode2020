import sys

with open("input.txt") as f:
    data = f.read().split("\n")

neighbors_to_check = set()


def check_loc(location, is_active):
    active_neighbors = 0
    x, y, z, w = location
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                for d in [-1, 0, 1]:
                    if not a == b == c == d == 0:
                        try:
                            if active[(x + a, y + b, z + c, w + d)]:
                                active_neighbors += 1
                            else:
                                if is_active:
                                    neighbors_to_check.add((x + a, y + b, z + c, w + d))

                        except KeyError:
                            if is_active:
                                neighbors_to_check.add((x + a, y + b, z + c, w + d))

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
        return active_neighbors == 3


# Formatted: (x,y,z,w) or (col,row,layer,weird)
active = dict()
for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == "#":
            active[(col, row, 0, 0)] = True

for i in range(6):
    active_copy = dict(active)
    for loc in active.keys():
        active_copy[loc] = check_loc(loc, is_active=True)
    while len(neighbors_to_check) > 0:
        to_check = neighbors_to_check.pop()
        active_copy[to_check] = check_loc(to_check, is_active=False)

    active = active_copy

print(list(active.values()).count(True))
