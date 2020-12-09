import sys

with open("input.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

forbidden_number = 1124361034
start = 0
while True:
    numbers = []
    for i in range(start,len(data)):
        numbers.append(data[i])
        if sum(numbers) == forbidden_number:
            print(min(numbers)+max(numbers))
            sys.exit()
        elif sum(numbers) > forbidden_number:
            start += 1
            break