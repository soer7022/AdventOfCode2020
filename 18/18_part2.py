with open("input.txt") as f:
    data = f.read().split("\n")


def evaluate(equation):
    while "(" in equation and ")" in equation:
        for i, c in enumerate(equation):
            if c == "(":
                start = i
            elif c == ")":
                end = i
                break
        equation = equation[0:start] + str(evaluate(equation[start + 1:end])) + equation[end + 1:]
    equation = equation.split(" ")

    while "+" in equation:
        i = equation.index("+")
        to_eval = "".join(equation[i - 1:i + 2])
        del equation[i - 1:i + 2]
        equation.insert(i - 1, str(eval(to_eval)))

    while len(equation) > 1:
        current_expr = "".join(equation[0:3])
        del equation[0:3]
        equation.insert(0, str(eval(current_expr)))
    return int(equation[0])


assert evaluate('1 + 2 * 3 + 4 * 5 + 6') == 231
assert evaluate('2 * 3 + (4 * 5)') == 46
assert evaluate('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
assert evaluate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
assert evaluate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

total = 0
for line in data:
    total += evaluate(line)

print(total)
