with open("input.txt") as f:
    data = [l.split("\n") for l in f.read().split("\n\n")]

total = 0
for group in data:
    answers = dict()
    for answer in group:
        for letter in answer:
            try:
                answers[letter] = answers[letter] + 1
            except KeyError:
                answers[letter] = 1
    for value in answers.values():
        if value == len(group):
            total += 1

print(total)