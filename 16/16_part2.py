with open("input.txt") as f:
    restrictions, your_ticket, nearby_tickets = f.read().split("\n\n")


def check_ticket(ticket):
    for n in [int(n) for n in ticket.split(",")]:
        if n not in allowed_numbers:
            return False
    return True


allowed_numbers_dict = dict()
allowed_numbers = set()
restrictions = restrictions.split("\n")
nearby_tickets = nearby_tickets.split("\n")
your_ticket = [int(v) for v in your_ticket.split("\n")[1].split(",")]
for line in restrictions:
    name, rules = line.split(": ")
    allowed_numbers_dict[name] = set()
    rules = rules.split(" or ")
    for rule in rules:
        start, end = rule.split("-")
        for i in range(int(start), int(end) + 1):
            allowed_numbers_dict[name].add(i)
            allowed_numbers.add(i)

nearby_tickets = nearby_tickets[1:]
nearby_tickets = list(filter(check_ticket, nearby_tickets))

possible_names = [[] for i in range(len(your_ticket))]
for index, number in enumerate(your_ticket):
    for key, value in allowed_numbers_dict.items():
        if number in value:
            possible_names[index].append(key)

for ticket in nearby_tickets:
    numbers = [int(n) for n in ticket.split(",")]
    for index, number in enumerate(numbers):
        for key, value in allowed_numbers_dict.items():
            if number not in value:
                possible_names[index].remove(key)

confirmed_names = ["" for i in range(len(your_ticket))]
finished = False
while not finished:
    finished = True
    for index, item in enumerate(possible_names):
        if len(item) == 1:
            found = item[0]
            confirmed_names[index] = found
            for name_list in possible_names:
                if len(name_list) != 0:
                    name_list.remove(found)
        elif len(item) == 0:
            continue
        else:
            finished = False
total = 1
for index, item in enumerate(confirmed_names):
    if "departure" in item:
        total = total * your_ticket[index]
print(total)
