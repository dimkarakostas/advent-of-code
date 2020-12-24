import operator
import functools
from copy import deepcopy
from math import sqrt

lines = [l.strip() for l in open('input20').readlines()]

tiles = {}
tid = None
for l in lines:
    if 'Tile' in l:
        tid = int(l.split()[1][:-1])
        tiles[tid] = []
    elif l != '':
        tiles[tid].append(l)
        tile_dimension = len(l)

dimension = int(sqrt(len(tiles.items())))

borders = {}
for tile_id, tile in tiles.items():
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

grid = [[None for _ in range(dimension)] for _ in range(dimension)]

grid[0][0] = corners[0]
grid[1][0] = neighbors[grid[0][0]].pop()
neighbors[grid[1][0]].remove(grid[0][0])
for i in range(1, dimension):
    grid[0][i] = neighbors[grid[0][i-1]].pop()
    neighbors[grid[0][i]].remove(grid[0][i-1])

    grid[1][i] = neighbors[grid[0][i]].intersection(neighbors[grid[1][i-1]]).pop()
    neighbors[grid[1][i]].remove(grid[1][i-1])
    neighbors[grid[1][i]].remove(grid[0][i])
    neighbors[grid[1][i-1]].remove(grid[1][i])
    neighbors[grid[0][i]].remove(grid[1][i])

for j in range(2, dimension):
    grid[j][0] = neighbors[grid[j-1][0]].pop()
    neighbors[grid[j][0]].remove(grid[j-1][0])

    for i in range(1, dimension):
        grid[j][i] = neighbors[grid[j][i-1]].intersection(neighbors[grid[j-1][i]]).pop()
        neighbors[grid[j][i]].remove(grid[j][i-1])
        neighbors[grid[j][i]].remove(grid[j-1][i])
        neighbors[grid[j][i-1]].remove(grid[j][i])
        neighbors[grid[j-1][i]].remove(grid[j][i])

def print_tile(tile):
    print('\n'.join([''.join(l) for l in tile]))

def rotate(tile):
    new_tile = []
    for i in range(1, len(tile) + 1):
        new_tile.append(''.join([tile[j][-1*i] for j in range(len(tile))]))
    return new_tile

def flip(tile, horizontal=True):
    new_tile = []
    if horizontal:
        for i in range(len(tile)-1, -1, -1):
            new_tile.append(tile[i])
    else:
        for line in tile:
            new_tile.append(line[::-1])
    return new_tile

# To find the initial orientation of 0, 0 uncomment the below lines and find it by hand
# print_tile(tiles[grid[0][0]])
# print()
# print_tile(tiles[grid[1][0]])
# print()
# print_tile(tiles[grid[0][1]])
grid[0][0] = rotate(flip(tiles[grid[0][0]], False))

perms = []
for fl in range(4):
    for rot in range(4):
        perms.append((fl, rot))

for i in range(1, dimension):
    prev_tile = grid[0][i-1]
    border = [l[-1] for l in prev_tile]
    tile = tiles[grid[0][i]]
    flag = True
    for (fl, rot) in perms:
        new_tile = deepcopy(tile)
        for _ in range(rot):
            new_tile = rotate(new_tile)
        if fl == 1:
            new_tile = flip(new_tile)
        elif fl == 2:
            new_tile = flip(new_tile, False)
        elif fl == 3:
            new_tile = flip(new_tile)
            new_tile = flip(new_tile, False)

        if [l[0] for l in new_tile] == border:
            flag = False
            break
    if flag:
        print('wrong first line', i)
    grid[0][i] = new_tile

for j in range(1, dimension):
    for i in range(dimension):
        border = grid[j-1][i][-1]
        tile = tiles[grid[j][i]]
        flag = True
        for (fl, rot) in perms:
            new_tile = deepcopy(tile)
            for _ in range(rot):
                new_tile = rotate(new_tile)
            if fl == 1:
                new_tile = flip(new_tile)
            elif fl == 2:
                new_tile = flip(new_tile, False)
            elif fl == 3:
                new_tile = flip(new_tile)
                new_tile = flip(new_tile, False)

            if new_tile[0] == border:
                flag = False
                break
        if flag:
            print('wrong', j, i)
        grid[j][i] = new_tile

complete_grid = []
for tile_line_idx in range(dimension):
    for inner_line_idx in range(1, tile_dimension-1):
        new_line = ''
        for tile_col_idx in range(dimension):
            new_line += grid[tile_line_idx][tile_col_idx][inner_line_idx][1:tile_dimension-1]
        complete_grid.append(new_line)

for (fl, rot) in perms:
    final_grid = deepcopy(complete_grid)
    for _ in range(rot):
        final_grid = rotate(final_grid)
    if fl == 1:
        final_grid = flip(final_grid)
    elif fl == 2:
        final_grid = flip(final_grid, False)
    elif fl == 3:
        final_grid = flip(final_grid)
        final_grid = flip(final_grid, False)

    non_empty = set()
    for x in range(len(final_grid)):
        for y in range(len(final_grid[0])):
            if final_grid[x][y] == '#':
                non_empty.add((x, y))

    monsters = set()
    found_monster = False
    while not found_monster:
        for (x, y) in non_empty:
            if x < len(final_grid) - 2 and 18 < y < len(final_grid[0]) - 1:
                candidates = [
                    (x+1, y+1),
                    (x+1, y),
                    (x+1, y-1),
                    (x+2, y-2),
                    (x+2, y-5),
                    (x+1, y-6),
                    (x+1, y-7),
                    (x+2, y-8),
                    (x+2, y-11),
                    (x+1, y-12),
                    (x+1, y-13),
                    (x+2, y-14),
                    (x+2, y-17),
                    (x+1, y-18),
                ]
                if all([c in non_empty for c in candidates]):
                    found_monster = True
                    monsters.add((x, y))
                    for (a, b) in candidates + [(x, y)]:
                        non_empty.remove((a, b))
                        final_grid[a] = final_grid[a][:b] + 'o' + final_grid[a][b+1:]
                    break
        found_monster = not found_monster

    if len(monsters):
        print('Part 2:', len(non_empty))
        break
