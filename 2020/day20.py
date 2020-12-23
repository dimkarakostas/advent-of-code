import operator
import functools
from math import sqrt

lines = [l.strip() for l in open('input20').readlines()]

tiles = []
for l in lines:
    if 'Tile' in l:
        tiles.append([int(l.split()[1][:-1]), []])
    elif l != '':
        tiles[-1][1].append(l)

borders = {}
for tile_id, tile in tiles:
    top = [idx for idx, t in enumerate(tile[0]) if t == '#']
    right = [idx for idx, t in enumerate(tile) if t[-1] == '#']
    bottom = [idx for idx, t in enumerate(tile[-1]) if t == '#']
    left = [idx for idx, t in enumerate(tile) if t[0] == '#']
    standard_border = [top, right, bottom, left]
    border_permutations = [
        [standard_border[(j-i) % 4] for j in range(4)] for i in range(4)
    ]

    flipped_vertical = [
        sorted([9-i for i in top]),
        left,
        sorted([9-i for i in bottom]),
        right
    ]
    border_permutations += [
        [flipped_vertical[(j-i) % 4] for j in range(4)] for i in range(4)
    ]
    flipped_horizontal = [
        bottom,
        sorted([9-i for i in right]),
        top,
        sorted([9-i for i in left]),
    ]
    border_permutations += [
        [flipped_horizontal[(j-i) % 4] for j in range(4)] for i in range(4)
    ]
    borders[tile_id] = border_permutations

neighbors = {k: set() for k in borders.keys()}
for tile_id in borders.keys():
    for perm in borders[tile_id]:
        for border in perm:
            for c_id in [k for k in borders.keys() if k != tile_id]:
                for c_perm_idx, c_perm in enumerate(borders[c_id]):
                    for c_border in c_perm:
                        if c_border == border:
                            neighbors[tile_id].add(c_id)

corners = [tid for tid in neighbors.keys() if len(neighbors[tid]) == 2]
print('Part 1:', functools.reduce(operator.mul, corners))
