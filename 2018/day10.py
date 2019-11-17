stars = []
with open('input10', 'r') as f:
    for line in f:
        splitted = line.split(',')
        stars.append({
            'position': [
                int(splitted[1].split('>')[0]),
                int(splitted[0].split('<')[-1]),
            ],
            'velocity': (
                int(splitted[2].split('>')[0]),
                int(splitted[1].split('<')[-1]),
            )
        })

min_entropy = 1000000000000
for second in range(11000):
    new_star_positions = []
    borders = {
        'left': 1000000000000,
        'up': 1000000000000,
        'right': 0,
        'down': 0,
    }

    for idx, star in enumerate(stars):
        position = (
            star['position'][0] + (second * star['velocity'][0]),
            star['position'][1] + (second * star['velocity'][1])
        )
        new_star_positions.append(position)
        if position[0] < borders['up']:
            borders['up'] = position[0]
        if position[0] > borders['down']:
            borders['down'] = position[0]
        if position[1] < borders['left']:
            borders['left'] = position[1]
        if position[1] > borders['right']:
            borders['right'] = position[1]

    box_size = (borders['right'] - borders['left']) * (borders['down'] - borders['up'])
    if box_size < min_entropy:
        min_entropy = box_size
        new_stars = new_star_positions
    else:
        break

print second - 1
line_offset = min([s[0] for s in new_stars])
column_offset = min([s[1] for s in new_stars])
lines = max([s[0] for s in new_stars]) - line_offset + 1
columns = max([s[1] for s in new_stars]) - column_offset + 1

board = [[] for _ in range(lines)]
for i in range(lines):
    board[i] = ['.' for _ in range(columns)]
for idx, star in enumerate(new_stars):
    line = star[0] - line_offset
    column = star[1] - column_offset
    board[line][column] = 'X'
print '\n'.join([''.join(i) for i in board])
