grid = []
with open('input8') as f:
    for line in f.readlines():
        grid.append([int(i) for i in list(line.strip())])

visible = 2*len(grid) + 2*len(grid[0]) - 4
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        elem = grid[i][j]
        if any([
            max(grid[i][:j]) < elem,
            max(grid[i][j+1:]) < elem,
            max([grid[idx][j] for idx in range(i)]) < elem,
            max([grid[idx][j] for idx in range(i+1, len(grid))]) < elem,
        ]):
            visible += 1

print('Part 1:', visible)

scores = set()
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        elem = grid[i][j]

        right = 0
        for neighbor in grid[i][j+1:]:
            right += 1
            if neighbor >= elem:
                break

        left = 0
        for neighbor in reversed(grid[i][:j]):
            left += 1
            if neighbor >= elem:
                break

        bottom = 0
        for neighbor in [grid[idx][j] for idx in range(i+1, len(grid))]:
            bottom += 1
            if neighbor >= elem:
                break

        top = 0
        for neighbor in reversed([grid[idx][j] for idx in range(i)]):
            top += 1
            if neighbor >= elem:
                break

        scores.add(right*left*top*bottom)

print('Part 2:', max(scores))
