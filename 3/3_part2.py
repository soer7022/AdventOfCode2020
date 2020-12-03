with open("input.txt") as f:
    data = [l.strip() for l in f.readlines()]


def traverse(down, right):
    count = 0
    width = len(data[0])
    height = len(data)
    i = 0
    curr_right = 0
    while i < height - 1:
        i += down
        curr_right += right
        curr_right = curr_right % width
        location = data[i][curr_right]
        if location == "#":
            count += 1
    return count


print(traverse(1, 1) * traverse(1, 3) * traverse(1, 5) * traverse(1, 7) * traverse(2, 1))
