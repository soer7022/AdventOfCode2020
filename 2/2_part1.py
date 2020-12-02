from itertools import groupby

data = []
with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]

valid = 0

for line in data:
    invalid = False
    constraints, password = line.split(": ")
    repetitions, letter = constraints.split(" ")
    min_reps, max_reps = [int(i) for i in repetitions.split("-")]
    letter_map = dict()
    if letter not in password:
        invalid = True
    if not invalid:
        for l in password:
            try:
                letter_map[l] += 1
            except KeyError:
                letter_map[l] = 1
        if not min_reps <= letter_map[letter] <= max_reps:
            invalid = True
    if not invalid:
        valid += 1

print(valid)
