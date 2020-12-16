spoken = [14,3,1,0,9,5]

curr_index = len(spoken)
last_spoken = dict()
for index, n in enumerate(spoken):
    last_spoken[n] = index + 1

spoken_before = set(spoken)
spoken_before.remove(spoken[len(spoken) - 1])
while curr_index < 30000000:
    prev_spoken = spoken[curr_index - 1]
    spoken_before_that = spoken[curr_index - 2]
    if prev_spoken == spoken_before_that:
        spoken.append(1)
    elif prev_spoken not in spoken_before:
        spoken.append(0)
    else:
        previous = (curr_index +1) - (last_spoken[prev_spoken] + 1)
        spoken.append(previous)
    spoken_before.add(prev_spoken)
    last_spoken[prev_spoken] = curr_index
    curr_index += 1

print(spoken[30000000-1])
