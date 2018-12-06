def distance(point, coordinate):
    return abs(point[0] - coordinate[0]) + abs(point[1] - coordinate[1])


with open('input6', 'r') as f:
    coordinates = [(int(i.split()[0][:-1]), int(i.split()[1].strip())) for i in f.readlines()]

limits = (
    max(coordinates, key=lambda p: p[0])[0] + 1,
    max(coordinates, key=lambda p: p[1])[1] + 1
)
board = [[] for _ in range(limits[1])]
for i in range(limits[1]):
    board[i] = [[-1, 10000, 0] for _ in range(limits[0])]

counters = [0 for _ in range(len(coordinates))]
for idx, c in enumerate(coordinates):
    for line in range(0, limits[1]):
        for column in range(0, limits[0]):
            (previous_idx, previous_dst, _) = board[line][column]
            dst = distance((column, line), c)
            if previous_dst >= dst:
                if previous_idx > -1:
                    counters[previous_idx] -= 1
                if previous_dst > dst:
                    board[line][column][0] = idx
                    board[line][column][1] = dst
                    counters[idx] += 1
                else:
                    board[line][column][0] = -1
            board[line][column][2] += dst

sums = 0
for line in range(0, limits[1]):
    counters[board[line][0][0]] -= 100000 if board[line][0][0] > -1 else 0
    counters[board[line][limits[0] - 1][0]] -= 100000 if board[line][limits[0] - 1][0] > -1 else 0
    for column in range(0, limits[0]):
        counters[board[0][column][0]] -= 100000 if board[0][column][0] > -1 else 0
        counters[board[limits[1] - 1][column][0]] -= 100000 if board[limits[1] - 1][column][0] > -1 else 0

        sums += 1 if board[line][column][2] < 10000 else 0

print 'Part 1:', max(counters)
print 'Part 2:', sums
