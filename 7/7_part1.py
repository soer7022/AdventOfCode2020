import networkx as nx
import matplotlib.pyplot as plt

with open("input.txt") as f:
    data = [l.split("s contain ") for l in f.read().split("\n")]

G = nx.DiGraph()

for line in data:
    outer_case = line[0]
    inner_cases = line[1].split(", ")
    # sanitize input
    outer_case = outer_case[::]
    G.add_node(outer_case)
    for case in inner_cases:
        case = case[2::]
        if case.endswith("s."):
            case = case[:-2]
        elif case.endswith("s") or case.endswith("."):
            case = case[:-1]
        G.add_node(case)
        G.add_edge(case, outer_case)
visited = set()
queue = list(nx.dfs_predecessors(G, "shiny gold bag"))
while len(queue) > 0:
    current = queue.pop(0)
    visited.add(current)
    for elem in nx.dfs_predecessors(G,current):
        if elem not in visited:
            queue.append(elem)


print(len(visited))
