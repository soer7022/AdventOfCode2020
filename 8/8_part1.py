with open("input.txt") as f:
    data = f.read().split("\n")

i = 0
acc = 0
seen = set()

while True:
    if i in seen:
        print(acc)
        break
    else:
        seen.add(i)
    raw_instruction = data[i]
    instruction, value = raw_instruction.split(" ")
    value = int(value)
    if instruction == "acc":
        acc += value
        i += 1
    elif instruction == "jmp":
        i += value
    else:
        i += 1
