def check_state(grid, x, x_dir, y, y_dir):
    if x+x_dir not in range(0, len(grid)) or y+y_dir not in range(0, len(grid[0])):
        return '.'
    return grid[x+x_dir][y+y_dir]

def check_line(grid, x, x_dir, y, y_dir):
    x += x_dir
    y += y_dir
    while x in range(0, len(grid)) and y in range(0, len(grid[0])):
        if grid[x][y] != '.':
            return grid[x][y]
        x += x_dir
        y += y_dir
    return '.'

def run_part(part, lines):
    if part == 1:
        check, bound = check_state, 3
    elif part == 2:
        check, bound = check_line, 4

    changing = True
    while changing:
        newlines = [[point for point in l] for l in lines]
        changing = False
        for x, line in enumerate(newlines):
            for y, point in enumerate(line):
                if point == '.':
                    continue
                elif point == 'L' and not any([
                        check(lines, x, i, y, j) == '#' for i in [-1, 0, 1] for j in [-1, 0, 1] if (i or j)
                    ]):
                    newlines[x][y], changing = '#', True
                elif point == '#' and sum([
                        check(lines, x, i, y, j) == '#' for i in [-1, 0, 1] for j in [-1, 0, 1] if (i or j)
                    ]) > bound:
                    newlines[x][y], changing = 'L', True
        lines = [[point for point in l] for l in newlines]
    return lines

og_lines = [list(l.strip()) for l in open('input11').readlines()]

lines = run_part(1, og_lines[:])
occupied = sum([point == '#' for l in lines for point in l])
print('Part 1:', occupied)

lines = run_part(2, og_lines[:])
occupied = sum([point == '#' for l in lines for point in l])
print('Part 2:', occupied)
