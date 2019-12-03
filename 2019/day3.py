wires = []
for l in open('input3').readlines():
    wires.append([(mvmt[0], int(mvmt[1:])) for mvmt in l.strip().split(',')])

points = [{}, {}]
for widx, w in enumerate(wires):
    x, y, steps = 0, 0, 0
    for direction, distance in w:
        for _ in range(distance):
            steps += 1
            x += 1 if direction == 'D' else -1 if direction == 'U' else 0
            y += 1 if direction == 'R' else -1 if direction == 'L' else 0
            points[widx][(x, y)] = steps

intersections = set(points[0].keys()).intersection(set(points[1].keys()))
print 'Part 1:', min([abs(p[0]) + abs(p[1]) for p in intersections])
print 'Part 2:', min([points[0][p] + points[1][p] for p in intersections])
