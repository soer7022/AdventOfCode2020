with open("input.txt") as f:
    p1, p2 = [player.split("\n") for player in f.read().split("\n\n")]
    p1.pop(0)
    p2.pop(0)
    p1 = [int(i) for i in p1]
    p2 = [int(i) for i in p2]


def play_game(p1_deck, p2_deck, game_id):
    hands_seen = set()
    round = 1
    # print(f"=== Game {game_id} ===")
    # print("")
    winner = True
    while not len(p1_deck) == 0 and not len(p2_deck) == 0:
        # print(f"-- Round {round} --")
        # print("Player 1's deck: " + ", ".join([str(s) for s in p1_deck]))
        # print("Player 2's deck: " + ", ".join([str(s) for s in p2_deck]))
        if (str(p1_deck), str(p2_deck)) in hands_seen:
            winner = True
            break
        hands_seen.add((str(p1_deck), str(p2_deck)))
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)
        # print(f"Player 1 plays: {p1_card}")
        # print(f"Player 2 plays: {p2_card}")

        if p1_card <= len(p1_deck) and p2_card <= len(p2_deck):
            # print("Playing a sub-game to determine the winner...")
            # print("")
            sub_p1_deck = p1_deck[0:p1_card]
            sub_p2_deck = p2_deck[0:p2_card]
            winner = play_game(sub_p1_deck, sub_p2_deck, game_id + 1)
            # print("")
            # print(f"...anyway, back to game {game_id}.")
        else:
            winner = p1_card > p2_card

        if winner:
            # print("Player 1 wins the round!")
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        else:
            # print("Player 2 wins the round!")
            p2_deck.append(p2_card)
            p2_deck.append(p1_card)
        round += 1
    return winner


overall_winner = p1 if play_game(p1, p2, 1) else p2
# print(overall_winner)

total = 0
for i in range(len(overall_winner), 0, -1):
    card = overall_winner.pop(0)
    total += card * i
print(total)
