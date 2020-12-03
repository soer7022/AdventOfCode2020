with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]

count = 0
width = len(data[0])
height = len(data)
i = 0
right = 0
while i < height - 1:
    i += 1
    right += 3
    right = right % width
    location = data[i][right]
    if location == "#":
        count += 1

print(count)
