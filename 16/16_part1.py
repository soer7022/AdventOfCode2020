with open("input.txt") as f:
    restrictions, your_ticket, nearby_tickets = f.read().split("\n\n")

allowed_numbers = set()
restrictions = restrictions.split("\n")
nearby_tickets = nearby_tickets.split("\n")
your_ticket = [int(v) for v in your_ticket.split("\n")[1].split(",")]
for line in restrictions:
    name, rules = line.split(": ")
    rules = rules.split(" or ")
    for rule in rules:
        start, end = rule.split("-")
        for i in range(int(start), int(end) + 1):
            allowed_numbers.add(i)

nearby_tickets = nearby_tickets[1:]
total = 0
for ticket in nearby_tickets:
    numbers = [int(n) for n in ticket.split(",")]
    for index, number in enumerate(numbers):
        if number not in allowed_numbers:
            total += number

print(total)