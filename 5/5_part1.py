with open("input.txt") as f:
    data = f.read().split("\n")

best = 0
for boarding_pass in data:
    actual_row = 0
    actual_col = 0
    low_row = 0
    high_row = 127
    low_col = 0
    high_col = 7
    count = 0
    for letter in boarding_pass:
        if count == 6:
            if letter == "F":
                actual_row = low_row
            elif letter == "B":
                actual_row = high_row
        elif count == 9:
            if letter == "L":
                actual_col = low_col
            elif letter == "R":
                actual_col = high_col

        if letter == "F":
            high_row = ((low_row + high_row) // 2)
        elif letter == "B":
            low_row = ((low_row + high_row + 1) // 2)
        elif letter == "L":
            high_col = ((low_col + high_col) // 2)
        elif letter == "R":
            low_col = ((low_col + high_col + 1) // 2)

        count += 1
    best = max(actual_row * 8 + actual_col, best)

print(best)
