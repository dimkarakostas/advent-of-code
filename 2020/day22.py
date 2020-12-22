from copy import deepcopy

lines = [l.strip() for l in open('input22').readlines()]

original_decks = [[]]
for l in lines[1:]:
    if l == 'Player 2:':
        original_decks.append([])
    elif l.isdigit():
        original_decks[-1].append(int(l))


def part_1(decks):
    while decks[0] and decks[1]:
        cards = [decks[0].pop(0), decks[1].pop(0)]
        winner = cards.index(max(cards))
        decks[winner] += [max(cards), min(cards)]

    winner = decks[0] if decks[0] else decks[1]
    return sum([item*(len(winner) - idx) for idx, item in enumerate(winner)])

print('Part 1:', part_1(deepcopy(original_decks)))

def part_2(decks):
    rounds = set()

    while decks[0] and decks[1] and (tuple(decks[0]), tuple(decks[1])) not in rounds:
        rounds.add((tuple(decks[0]), tuple(decks[1])))

        cards = [decks[0].pop(0), decks[1].pop(0)]
        if any([cards[i] > len(decks[i]) for i in (0, 1)]):
            winner = cards.index(max(cards))
        else:
            winner, _ = part_2([decks[0][:cards[0]], decks[1][:cards[1]]])
        decks[winner] += cards if winner == 0 else cards[::-1]

    winner = 0 if decks[0] else 1
    return winner, sum([item*(len(decks[winner]) - idx) for idx, item in enumerate(decks[winner])])

print('Part 2:', part_2(deepcopy(original_decks))[1])
