from pyformlang.cfg import Production, Variable, Terminal, CFG, Epsilon

with open("input.txt") as f:
    rules, data = f.read().split("\n\n")

rules = rules.split("\n")
data = [item.strip() for item in data.split("\n")]
variables = set()
productions = set()
term_a = Terminal("a")
term_b = Terminal("b")

rule_map = dict()
for rule in rules:
    no, item = rule.split(": ")
    rule_map[int(no)] = item

for index, rule in rule_map.items():
    variables.add(Variable(index))
    if "a" in rule:
        productions.add(Production(Variable(index), [term_a]))
    elif "b" in rule:
        productions.add(Production(Variable(index), [term_b]))
    else:
        to_add = rule.split(" | ")
        for item in to_add:
            productions.add(Production(Variable(index), [Variable(int(x)) for x in item.split(" ")]))

cfg = CFG(variables, {term_a, term_b}, Variable(0), productions)

total = 0
for item in data:
    print(item)
    if cfg.contains(item):
        total += 1

print(total)
