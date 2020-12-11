with open("input.txt") as f:
    data = [int(i) for i in f.read().split("\n")]
data.sort()

diff_one = 0
diff_three = 1
current_jolt = 0
for adapter in data:
    diff = adapter - current_jolt
    current_jolt = adapter
    diff_three += diff == 3
    diff_one += diff == 1

print(diff_one * diff_three, diff_one, diff_three)
