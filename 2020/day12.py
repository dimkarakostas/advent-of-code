def move(direction, amount, h, v):
    if direction in ('E', 'W'):
        h += amount if direction == 'E' else -1 * amount
    elif direction in ('N', 'S'):
        v += amount if direction == 'N' else -1 * amount
    return h, v


lines = [(l[0], int(l[1:].strip())) for l in open('input12').readlines()]

directions = ['N', 'E', 'S', 'W']

face = 1
horizontal, vertical = 0, 0
for (movement, amount) in lines:
    if movement == 'F':
        horizontal, vertical = move(directions[face], amount, horizontal, vertical)
    elif movement in directions:
        horizontal, vertical = move(movement, amount, horizontal, vertical)
    else:
        degrees = int(amount/90) if movement == 'R' else int(amount / -90)
        face = (face + degrees) % 4
print('Part 1:', abs(vertical) + abs(horizontal))

horizontal, vertical = 0, 0
waypoint_h, waypoint_v = 10, 1
for (movement, amount) in lines:
    if movement == 'F':
        horizontal += amount * waypoint_h
        vertical += amount * waypoint_v
    elif movement in directions:
        waypoint_h, waypoint_v = move(movement, amount, waypoint_h, waypoint_v)
    else:
        for _ in range(int(amount / 90) % 4):
            waypoint_h, waypoint_v = waypoint_v, -1 * waypoint_h
            if movement == 'L':
                waypoint_h, waypoint_v = -1 * waypoint_h, -1 * waypoint_v
print('Part 2:', abs(vertical) + abs(horizontal))
