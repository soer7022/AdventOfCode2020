with open("input.txt") as f:
    data = [l.split(" = ") for l in f.read().split("\n")]
print(data)
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
memory = dict()
for instr in data:
    if instr[0] == "mask":
        mask = instr[1]
    else:
        address = int(instr[0][4:-1])
        value = format(int(instr[1]), 'b').zfill(len(mask))
        final_value = ""
        for i in range(len(value)):
            if mask[i] == "X":
                final_value += value[i]
            else:
                final_value += mask[i]
        memory[address] = final_value

total = 0
for value in memory.values():
    total += int(value,2)

print(total)