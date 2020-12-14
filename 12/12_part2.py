with open("input.txt") as f:
    data = [(l[0], int(l[1:])) for l in f.read().split("\n")]
directions = ["N", "E", "S", "W"]
facing = 1
north = 0
east = 0
for instr in data:
    dir_instr = instr[0]
    num = instr[1]
    if dir_instr == "F":
        dir_instr = directions[facing]
    if dir_instr == "L":
        facing = (facing - (num//90)) % len(directions)
    if dir_instr == "R":
        facing = (facing + (num//90)) % len(directions)
    if dir_instr == "N":
        north += num
    if dir_instr == "E":
        east += num
    if dir_instr == "W":
        east -= num
    if dir_instr == "S":
        north -= num

print(abs(north) + abs(east))

