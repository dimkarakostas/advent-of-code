import copy


class Wagon:
    def __init__(self, id, x, y, d):
        self.id = id
        self.x = x
        self.y = y
        self.direction = d
        self.intersection_counter = 0

    def __repr__(self):
        return '{}: ({}, {}) {}'.format(self.id, self.x, self.y, self.direction)


grid = []
with open('input13', 'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip('\n')))
    grid.append([' ' for _ in grid[1]])
    grid.insert(0, [' ' for _ in grid[1]])
    for line in grid:
        line.insert(0, ' ')
        line.append(' ')

wagons = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] in ('<', '>', 'v', '^'):
            wagons.append(Wagon(len(wagons), x, y, grid[x][y]))
            grid[x][y] = len(wagons) - 1

pure_grid = copy.deepcopy(grid)
for w in wagons:
    (x, y) = (w.x, w.y)
    (u, d, l, r) = (grid[x - 1][y], grid[x + 1][y], grid[x][y - 1], grid[x][y + 1])

    if u in (' ', '-'):
        if r in (' ', '|'):
            pure_grid[x][y] = '\\'
        elif l in (' ', '|'):
            pure_grid[x][y] = '/'
        else:
            pure_grid[x][y] = '-'
    elif d in (' ', '-'):
        if r in (' ', '|'):
            pure_grid[x][y] = '/'
        elif l in (' ', '|'):
            pure_grid[x][y] = '\\'
        else:
            pure_grid[x][y] = '-'
    elif r in (' ', '|'):
        if u in (' ', '-'):
            pure_grid[x][y] = '\\'
        elif d in (' ', '-'):
            pure_grid[x][y] = '/'
        else:
            pure_grid[x][y] = '|'
    elif l in (' ', '|'):
        if u in (' ', '-'):
            pure_grid[x][y] = '/'
        elif d in (' ', '-'):
            pure_grid[x][y] = '\\'
        else:
            pure_grid[x][y] = '|'
    else:
        pure_grid[x][y] = '+'

INITIAL_WAGONS = len(wagons)
crashes = []
crashed_wagons = []


def allow_move(idx, w):
    (x, y) = (w.x, w.y)
    (u, d, l, r) = (pure_grid[x - 1][y], pure_grid[x + 1][y], pure_grid[x][y - 1], pure_grid[x][y + 1])
    if any([
        u in (' ', '-') and w.direction == '^',
        d in (' ', '-') and w.direction == 'v',
        r in (' ', '|') and w.direction == '>',
        l in (' ', '|') and w.direction == '<'
    ]):
        print idx, w
        grid[w.x][w.y] = w.id
        for line in grid:
            print ''.join([str(k) for k in line])
        return False
    return True


def handle_crash(idx, w):
    crashes.append(((w.y - 1, w.x - 1), idx))
    for wag in wagons:
        if wag.id == grid[w.x][w.y]:
            crashed_wagons.append(wag)
            break
    crashed_wagons.append(w)
    grid[w.x][w.y] = pure_grid[w.x][w.y]


idx = 0
while True:
    idx += 1
    wagons = [w for w in wagons if w.id not in [wag.id for wag in crashed_wagons]]
    if len(wagons) < 2:
        break
    wagons = sorted(wagons, key=lambda w: (w.x, w.y))
    for i, w in enumerate(wagons):
        if w in crashed_wagons:
            continue
        grid[w.x][w.y] = pure_grid[w.x][w.y]
        if w.direction == '<':
            assert allow_move(idx, w)
            w.y -= 1
            if grid[w.x][w.y] in range(INITIAL_WAGONS):
                handle_crash(idx, w)
            else:
                if grid[w.x][w.y] == '/':
                    w.direction = 'v'
                elif grid[w.x][w.y] == '\\':
                    w.direction = '^'
                elif grid[w.x][w.y] == '+':
                    if w.intersection_counter % 3 == 0:
                        w.direction = 'v'
                    elif w.intersection_counter % 3 == 2:
                        w.direction = '^'
                    w.intersection_counter += 1
                grid[w.x][w.y] = w.id
        elif w.direction == '>':
            assert allow_move(idx, w)
            w.y += 1
            if grid[w.x][w.y] in range(INITIAL_WAGONS):
                handle_crash(idx, w)
            else:
                if grid[w.x][w.y] == '/':
                    w.direction = '^'
                elif grid[w.x][w.y] == '\\':
                    w.direction = 'v'
                elif grid[w.x][w.y] == '+':
                    if w.intersection_counter % 3 == 0:
                        w.direction = '^'
                    elif w.intersection_counter % 3 == 2:
                        w.direction = 'v'
                    w.intersection_counter += 1
                grid[w.x][w.y] = w.id
        elif w.direction == 'v':
            assert allow_move(idx, w)
            w.x += 1
            if grid[w.x][w.y] in range(INITIAL_WAGONS):
                handle_crash(idx, w)
            else:
                if grid[w.x][w.y] == '/':
                    w.direction = '<'
                elif grid[w.x][w.y] == '\\':
                    w.direction = '>'
                elif grid[w.x][w.y] == '+':
                    if w.intersection_counter % 3 == 0:
                        w.direction = '>'
                    elif w.intersection_counter % 3 == 2:
                        w.direction = '<'
                    w.intersection_counter += 1
                grid[w.x][w.y] = w.id
        elif w.direction == '^':
            assert allow_move(idx, w)
            w.x -= 1
            if grid[w.x][w.y] in range(INITIAL_WAGONS):
                handle_crash(idx, w)
            else:
                if grid[w.x][w.y] == '/':
                    w.direction = '>'
                elif grid[w.x][w.y] == '\\':
                    w.direction = '<'
                elif grid[w.x][w.y] == '+':
                    if w.intersection_counter % 3 == 0:
                        w.direction = '<'
                    elif w.intersection_counter % 3 == 2:
                        w.direction = '>'
                    w.intersection_counter += 1
                grid[w.x][w.y] = w.id

print 'Crash place:', crashes[0][0]
print 'Final wagon:', (wagons[0].y - 1, wagons[0].x - 1)
