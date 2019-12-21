from collections import defaultdict
from string import ascii_uppercase

grid = [list(ln[:-1]) for ln in open('input20').readlines()]
portals, portal_paths = [], defaultdict(list)
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] in list(ascii_uppercase):
            if grid[x + 1][y] in list(ascii_uppercase):
                portal = ''.join([grid[x][y], grid[x + 1][y]])
                if portal not in portals:
                    portals.append(portal)
                if x == 0 or grid[x - 1][y] == ' ':
                    grid[x + 2][y] = portals.index(portal)
                    portal_paths[portals.index(portal)].append((x + 2, y))
                else:
                    grid[x - 1][y] = portals.index(portal)
                    portal_paths[portals.index(portal)].append((x - 1, y))
                grid[x + 1][y] = ' '
            elif grid[x][y + 1] in list(ascii_uppercase):
                portal = ''.join([grid[x][y], grid[x][y + 1]])
                if portal not in portals:
                    portals.append(portal)
                if y == 0 or grid[x][y - 1] == ' ':
                    grid[x][y + 2] = portals.index(portal)
                    portal_paths[portals.index(portal)].append((x, y + 2))
                else:
                    grid[x][y - 1] = portals.index(portal)
                    portal_paths[portals.index(portal)].append((x, y - 1))
                grid[x][y + 1] = ' '
            grid[x][y] = ' '

entrance = portal_paths[portals.index('AA')][0]
exit = portal_paths[portals.index('ZZ')][0]
horizon, visited, steps = set([entrance]), set(), 0
while exit not in horizon:
    new_horizon = set()
    for (x, y) in horizon:
        for idx in (-1, 1):
            if grid[x + idx][y] not in (' ', '#'):
                new_horizon.add((x + idx, y))
            if grid[x][y + idx] not in (' ', '#'):
                new_horizon.add((x, y + idx))
        if grid[x][y] in range(len(portals)):
            for portal_cell in portal_paths[grid[x][y]]:
                new_horizon.add(portal_cell)
        visited.add((x, y))
    horizon = new_horizon.difference(visited)
    steps += 1
print 'Part 1:', steps

horizon, visited, steps = set([(entrance[0], entrance[1], 0)]), set(), 0
while (exit[0], exit[1], 0) not in horizon:
    new_horizon = set()
    for (x, y, level) in horizon:
        for idx in (-1, 1):
            if grid[x + idx][y] not in (' ', '#'):
                new_horizon.add((x + idx, y, level))
            if grid[x][y + idx] not in (' ', '#'):
                new_horizon.add((x, y + idx, level))

        if grid[x][y] in range(len(portals)):
            if x in (2, len(grid) - 3) or y in (2, len(grid[0]) - 3):
                new_level = level - 1
            else:
                new_level = level + 1
            if new_level >= 0:
                for cell in portal_paths[grid[x][y]]:
                    if cell != (x, y):
                        if cell[0] in (2, len(grid) - 3) or cell[1] in (2, len(grid[0]) - 3):
                            new_horizon.add((cell[0], cell[1], new_level + 1))
                        else:
                            new_horizon.add((cell[0], cell[1], new_level - 1))
        visited.add((x, y, level))
    horizon = new_horizon.difference(visited)
    steps += 1
print 'Part 2:', steps
