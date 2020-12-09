with open("input.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

current_start = 0
preamble_length = 25

while True:
    correct = False
    target = data[current_start+preamble_length]
    for i in range(current_start, current_start + preamble_length):
        for j in range(current_start,current_start + preamble_length):
            if i == j:
                pass
            if data[i] + data[j] == target:
                correct = True
    if correct:
        current_start += 1
    else:
        print(target)
        break