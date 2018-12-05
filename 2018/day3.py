with open('input3', 'r') as f:
    counter = 0
    pieces = []
    for l in f.readlines():
        counter += 1
        parts = l.split()
        margins = parts[2].split(',')
        dimensions = parts[3].split('x')
        ln = (
            int(margins[0]),
            int(margins[1].strip(':')),
            int(dimensions[0]),
            int(dimensions[1])
        )
        pieces.append({
            'horizontal': (ln[0], ln[0] + ln[2]),
            'vertical': (ln[1], ln[1] + ln[3]),
            'id': counter
        })

limits = (
    max(pieces, key=lambda p: p['horizontal'][1])['horizontal'][1],
    max(pieces, key=lambda p: p['vertical'][1])['vertical'][1]
)
board = [[] for i in range(limits[1])]
for i in range(limits[1]):
    board[i] = [[] for _ in range(limits[0])]

overlaps = [False for _ in range(len(pieces))]
total = 0
for p in pieces:
    for h in range(p['horizontal'][0], p['horizontal'][1]):
        for v in range(p['vertical'][0], p['vertical'][1]):
            if board[v][h]:
                if len(board[v][h]) == 1:
                    total += 1
                overlaps[p['id'] - 1] = True
                overlaps[board[v][h][-1]] = True
            board[v][h].append(p['id'] - 1)
print 'Part1:', total
print 'Part2:', ''.join([str(i + 1) for i, ov in enumerate(overlaps) if not ov])
