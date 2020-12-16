with open("input.txt") as f:
    data = [(l[0], int(l[1:])) for l in f.read().split("\n")]
north = 0
east = 0
w_north = 1
w_east = 10
for instr in data:
    dir_instr = instr[0]
    num = instr[1]
    if dir_instr == "F":
        north += num * w_north
        east += num * w_east
    if dir_instr == "L":
        while num:
            w_east, w_north = -w_north, w_east
            num -= 90
    if dir_instr == "R":
        while num:
            w_east, w_north = w_north, -w_east
            num -= 90
    if dir_instr == "N":
        w_north += num
    if dir_instr == "E":
        w_east += num
    if dir_instr == "W":
        w_east -= num
    if dir_instr == "S":
        w_north -= num
    print(instr)
    print(w_east, w_north)
    print()

print(abs(north) + abs(east))
