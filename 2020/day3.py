lines = [l.strip() for l in open('input3').readlines()]

def get_trees(x_s, y_s):
    trees, x, y = 0, 0, 0
    while y < len(lines):
        trees += lines[y][x] == '#'
        x = (x + x_s) % len(lines[0])
        y += y_s
    return trees

print('Part 1:', get_trees(3, 1))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1
for (x_s, y_s) in slopes:
    total *= get_trees(x_s, y_s)

print('Part 2:', total)
