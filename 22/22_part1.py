with open("input.txt") as f:
    p1, p2 = [player.split("\n") for player in f.read().split("\n\n")]
    p1.pop(0)
    p2.pop(0)
    p1 = [int(i) for i in p1]
    p2 = [int(i) for i in p2]
round = 1
winner = ""
while not len(p1) == 0 and not len(p2) == 0:
    print(f"-- Round {round} --")
    print("Player 1's deck: " + ", ".join([str(s) for s in p1]))
    print("Player 2's deck: " + ", ".join([str(s) for s in p2]))
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)
    print(f"Player 1 plays: {p1_card}")
    print(f"Player 2 plays: {p2_card}")
    if p1_card > p2_card:
        p1.append(p1_card)
        p1.append(p2_card)
        print("Player 1 wins the round!")
        winner = p1

    else:
        p2.append(p2_card)
        p2.append(p1_card)
        print("Player 2 wins the round!")
        winner = p2

    print("")
    round += 1

print("== Post-game results ==")
print("Player 1's deck: " + ", ".join([str(s) for s in p1]))
print("Player 2's deck: " + ", ".join([str(s) for s in p2]))
total = 0
for i in range(len(winner),0,-1):
    card = winner.pop(0)
    total += card* i
print(total)