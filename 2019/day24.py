grid = tuple([tuple(ln.strip()) for ln in open('input24').readlines()])

snapshots = set()
while grid not in snapshots:
    snapshots.add(grid)
    new_grid = []
    for x, ln in enumerate(grid):
        new_ln = []
        for y, cell in enumerate(ln):
            adjacent_bugs = sum([
                1 if x + 1 < len(grid) and grid[x + 1][y] == '#' else 0,
                1 if x > 0 and grid[x - 1][y] == '#' else 0,
                1 if y + 1 < len(grid[0]) and grid[x][y + 1] == '#' else 0,
                1 if y > 0 and grid[x][y - 1] == '#' else 0
            ])
            new_ln.append('#' if (adjacent_bugs == 1) or (cell == '.' and adjacent_bugs == 2) else '.')
        new_grid.append(tuple(new_ln))
    grid = tuple(new_grid)

biodiversity = 0
for x, ln in enumerate(grid):
    for y, cell in enumerate(ln):
        if cell == '#':
            biodiversity += 2**(x * len(ln) + y)
print 'Part 1:', biodiversity
