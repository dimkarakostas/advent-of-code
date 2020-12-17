import itertools

lines = [l.strip() for l in open('input17').readlines()]

def get_active_neighbours(active_set, node):
    dimension_points = [(i-1, i, i+1) for i in node]

    active_sum = 0
    for element in itertools.product(*dimension_points):
        if element != node and element in active_set:
            active_sum += 1
    return active_sum

def game_of_life(dimensions=2, cycles=6):
    active = set()
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == '#':
                active.add((x, y) + (0,) * (dimensions-2))

    for _ in range(cycles):
        borders = [(
            min([n[idx] for n in active]) - 1,
            max([n[idx] for n in active]) + 1
        ) for idx in range(dimensions)]

        dimension_points = [range(bot, top+1) for (bot, top) in borders]

        next_active = set()
        for node in itertools.product(*dimension_points):
            if any([
                node in active and get_active_neighbours(active, node) in (2, 3),
                node not in active and get_active_neighbours(active, node) == 3
            ]):
                next_active.add(node)
        active = next_active

    return(len(active))

print('Part 1:', game_of_life(3))
print('Part 2:', game_of_life(4))
