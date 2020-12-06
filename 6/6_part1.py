with open("input.txt") as f:
    data = [l.split("\n") for l in f.read().split("\n\n")]

total = 0
for group in data:
    answers = set()
    for answer in group:
        for letter in answer:
            answers.add(letter)
    total += len(answers)

print(total)