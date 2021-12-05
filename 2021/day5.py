import re
from collections import defaultdict

regex = re.compile('(\d+),(\d+) -> (\d+),(\d+)')

lines = [l.strip() for l in open('input5').readlines()]

points_1 = defaultdict(int)
points_2 = defaultdict(int)
for line in lines:
    y1, x1, y2, x2 = (int(i) for i in regex.search(line).groups())

    if (x1 == x2) or (y1 == y2):
        for y in range(min(y1, y2), max(y1, y2)+1):
            for x in range(min(x1, x2), max(x1, x2)+1):
                points_1[(x, y)] += 1
                points_2[(x, y)] += 1
    elif (x1 < x2 and y1 < y2) or (x2 < x1 and y2 < y1):
        y = min(y1, y2)
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points_2[(x, y)] += 1
            y += 1
    else:
        x = max(x1, x2)
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points_2[(x, y)] += 1
            x -= 1

print('Part 1:', len([p for p in points_1.values() if p > 1]))
print('Part 2:', len([p for p in points_2.values() if p > 1]))
