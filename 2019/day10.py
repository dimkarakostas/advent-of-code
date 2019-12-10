from math import atan2, degrees, sqrt
from collections import defaultdict

asteroids = []
for y, l in enumerate(open('input10').readlines()):
    for x, a in enumerate(l):
        if a == '#':
            asteroids.append((x, y))

rel_positions, mx, chosen = defaultdict(list), 0, ()
for idx, a in enumerate(asteroids):
    angles = set()
    for b in asteroids:
        if a == b:
            continue
        divx, divy = b[0] - a[0], b[1] - a[1]
        angle = degrees(atan2(divx, -1 * divy))
        angle += 360 if angle < 0 else 0
        dist = sqrt(divx**2 + divy**2)
        rel_positions[a].append((angle, dist, b))
        if angle not in angles:
            angles.add(angle)
    if len(angles) > mx:
        mx, chosen = len(angles), a
print 'Part 1:', mx

pos, idx, vaporized = sorted(rel_positions[chosen]), 0, []
for _ in range(200):
    vaporized.append(pos[idx])
    while pos[idx][0] == vaporized[-1][0] or pos[idx] in vaporized:
        idx += 1
print 'Part 2:', vaporized[-1][2][0] * 100 + vaporized[-1][2][1]
