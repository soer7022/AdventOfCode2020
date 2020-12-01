data = []
with open('input.txt') as f:
    data = [int(i) for i in f.readlines()]

for i in data:
    for j in data:
        for k in data:
            if i + j + k == 2020:
                print(i, j,k)
