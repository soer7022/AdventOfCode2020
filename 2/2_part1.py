data = []
with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]

valid = 0

for line in data:
    invalid = False
    constraints, password = line.split(": ")
    repetitions, letter = constraints.split(" ")
    min_reps, max_reps = [int(i) for i in repetitions.split("-")]
    if min_reps <= password.count(letter) <= max_reps:
        valid += 1

print(valid)
