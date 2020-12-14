with open("input.txt") as f:
    departure, data = f.read().split("\n")
    departure = int(departure)
    data = [int(i) for i in data.split(",") if i != "x"]

best = (0,10000000000000)
# This is probably too slow
for bus in data:
    curr_timestamp = bus
    while curr_timestamp < departure:
        curr_timestamp += bus
    if curr_timestamp - departure < best[1]:
        best = (bus,curr_timestamp-departure)

print(best[0]*best[1])

