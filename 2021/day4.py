from collections import defaultdict

lines = [l.strip() for l in open('input4').readlines()]

positions = defaultdict(list)
boards = [[]]
for l in lines[2:]:
    if l == '':
        boards.append([])
    else:
        line = l.split()
        for idx, num in enumerate(line):
            positions[num].append((len(boards) - 1, len(boards[-1]), idx))
        boards[-1].append(line)

bingos = []
for num in lines[0].split(','):
    for (b, x, y) in positions[num]:
        if b not in [i[1] for i in bingos]:
            boards[b][x][y] = ''
            if not(''.join(boards[b][x]) and ''.join([r[y] for r in boards[b]])):
                bingos.append((num, b))

def compute_score(num, board):
    remaining = []
    for x in board:
        for y in x:
            if y != '':
                remaining.append(int(y))
    return num * sum(remaining)

(num, board_idx) = bingos[0]
print('Part 1:', compute_score(int(num), boards[board_idx]))

(num, board_idx) = bingos[-1]
print('Part 2:', compute_score(int(num), boards[board_idx]))
