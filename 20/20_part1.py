with open("input.txt") as f:
    data = f.read().split("\n\n")


def find_possible_edges(tile_no):
    possible_edges = []
    tile = tile_map[tile_no]
    possible_edges.append(tile[0])
    possible_edges.append(tile[-1])
    left_edge = ""
    right_edge = ""
    for line in tile:
        left_edge += line[0]
        right_edge += line[-1]
    possible_edges.append(left_edge)
    possible_edges.append(right_edge)

    for i in range(4):
        possible_edges.append(possible_edges[i][::-1])

    return possible_edges


tile_map = dict()

for line in data:
    tile_lines = line.split("\n")
    tile_id = int(tile_lines[0].split(" ")[1][:-1])
    tile_map[tile_id] = [line for line in tile_lines[1:]]

total = 1
for tile_id in tile_map.keys():
    edges = find_possible_edges(tile_id)
    matches = 0
    for tile_id2 in tile_map.keys():
        if tile_id == tile_id2:
            continue
        edges_to_check = find_possible_edges(tile_id2)
        for edge in edges_to_check:
            if edge in edges:
                matches += 1

    if matches == 4:
        total *= tile_id

print(total)
