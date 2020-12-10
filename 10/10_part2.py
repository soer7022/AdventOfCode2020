with open("input.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

data.append(0)
data.append(max(data)+3)
data.sort()
combinations = [0] * len(data)
combinations[0] = 1
for i in range(1,len(data)):
    for j in range(0,i):
        diff = data[i]-data[j]
        if diff <= 3:
            combinations[i] += combinations[j]


print(combinations[-1])