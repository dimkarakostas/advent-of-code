from collections import defaultdict

lines = [l.strip() for l in open('input24').readlines()]

black = set()
for line in lines:
    c, r = 0, 0
    idx = 0
    while idx < len(line):
        move = line[idx]
        idx += 1
        if move in ['n', 's']:
            move += line[idx]
            idx += 1

        if move in ['e', 'w']:
            c += 1 if move == 'e' else -1
        elif move in ['nw', 'sw']:
            if r % 2 == 1:
                c -= 1
            r += 1 if move == 'sw' else -1
        elif move in ['ne', 'se']:
            if r % 2 == 0:
                c += 1
            r += 1 if move == 'se' else -1
    if (c, r) in black:
        black.remove((c, r))
    else:
        black.add((c, r))
print('Part 1:', len(black))

for _ in range(100):
    new_black = set()
    black_neighbors = defaultdict(int)
    for (c, r) in black:
        if r % 2 == 0:
            neighbors = [
                (c, r-1),
                (c-1, r),
                (c, r+1),
                (c+1, r-1),
                (c+1, r),
                (c+1, r+1),
            ]
        else:
            neighbors = [
                (c-1, r-1),
                (c-1, r),
                (c-1, r + 1),
                (c, r - 1),
                (c+1, r),
                (c, r + 1),
            ]
        if sum([n in black for n in neighbors]) in [1, 2]:
            new_black.add((c, r))
        for n in neighbors:
            black_neighbors[n] += 1
    for tile, neighbors in black_neighbors.items():
        if neighbors == 2:
            new_black.add(tile)
    black = new_black
print('Part 2:', len(black))
