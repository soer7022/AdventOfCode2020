data = []
with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]

valid = 0

for line in data:
    invalid = False
    constraints, password = line.split(": ")
    repetitions, letter = constraints.split(" ")
    min_reps, max_reps = [int(i) for i in repetitions.split("-")]
    found_letter = False
    if password[min_reps - 1] == letter:
        found_letter = True
    if password[max_reps - 1] == letter:
        if found_letter:
            invalid = True
    elif not found_letter:
        invalid = True

    if not invalid:
        valid += 1

print(valid)
