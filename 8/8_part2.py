with open("input.txt") as f:
    data = f.read().split("\n")


for j in range(len(data)):
    i = 0
    acc = 0
    seen = set()
    data_copy = list(data)
    current_line = data_copy[j]
    correct = True
    if "jmp" in current_line:
        current_line = current_line.replace("jmp", "nop")
        data_copy[j] = current_line
    elif "nop" in current_line:
        current_line = current_line.replace("nop", "jmp")
        data_copy[j] = current_line
    while i < len(data):
        if i in seen:
            correct = False
            break
        else:
            seen.add(i)
        raw_instruction = data_copy[i]
        instruction, value = raw_instruction.split(" ")
        value = int(value)
        if instruction == "acc":
            acc += value
            i += 1
        elif instruction == "jmp":
            i += value
        else:
            i += 1

    if correct:
        print(data_copy)
        print(acc)