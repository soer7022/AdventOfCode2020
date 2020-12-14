with open("input.txt") as f:
    data = [l.split(" = ") for l in f.read().split("\n")]


mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
memory = dict()
for instr in data:
    if instr[0] == "mask":
        mask = instr[1]
    else:
        address = format(int(instr[0][4:-1]), 'b').zfill(len(mask))
        value = format(int(instr[1]), 'b').zfill(len(mask))

        final_addr = ""
        for i in range(len(value)):
            if mask[i] == "0":
                final_addr += address[i]
            else:
                final_addr += mask[i]
        addr_list = []
        to_check = [final_addr]
        while len(to_check) > 0:
            curr_elem = to_check.pop()
            if "X" not in curr_elem:
                addr_list.append(curr_elem)
                continue
            for i in range(len(curr_elem)):
                if curr_elem[i] == "X":
                    to_check.append(curr_elem[:i] + "0" + curr_elem[i+1:])
                    to_check.append(curr_elem[:i] + "1" + curr_elem[i+1:])
                    break
        for addr in addr_list:
            memory[int(addr,2)] = value
total = 0
for value in memory.values():
    total += int(value, 2)

print(total)
