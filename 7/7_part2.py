import networkx as nx
import matplotlib.pyplot as plt

with open("input.txt") as f:
    data = [l.split("s contain ") for l in f.read().split("\n")]
graph = {"no other bags.": []}
for line in data:
    outer_case = line[0]
    inner_cases = line[1].split(", ")
    # sanitize input
    outer_case = outer_case[::]
    graph[outer_case] = []
    for case in inner_cases:
        if case != "no other bags.":
            number_inside = int(case[0])
            case = case[2::]
            if case.endswith("s."):
                case = case[:-2]
            elif case.endswith("s") or case.endswith("."):
                case = case[:-1]
            graph[outer_case].append((case, number_inside))


def find_cases_within(bag):
    return 1 + sum(num * find_cases_within(bag) for bag, num in graph[bag])


number = find_cases_within("shiny gold bag")

print(number - 1)
