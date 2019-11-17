border = 300
inp = 7689

grid = []
for x in range(border):
    grid.append([])
    for y in range(border):
        cell_power = ((((((x + 10) * y) + inp) * (x + 10)) / 100) % 10) - 5
        grid[x].append(cell_power)

(max_cell_3, max_subgrid_power_3) = ((0, 0), 0)
(max_cell, max_subgrid_power, max_size) = ((0, 0), 0, 0)
power_grid = [[[] for _ in range(border)] for _ in range(border)]
for x in range(border):
    for y in range(border):
        power_grid[x][y] = [0, grid[x][y]]
        for size in range(2, border + 1):
            subgrid_power = power_grid[x][y][-1]
            for i in range(size - 1):
                try:
                    subgrid_power += grid[x + i][y + size - 1]
                except IndexError:
                    pass
            for i in range(size):
                try:
                    subgrid_power += grid[x + size - 1][y + i]
                except IndexError:
                    pass
            power_grid[x][y].append(subgrid_power)
            if size == 3:
                if subgrid_power > max_subgrid_power_3:
                    (max_cell_3, max_subgrid_power_3) = ((x, y), subgrid_power)
            if subgrid_power > max_subgrid_power:
                (max_cell, max_subgrid_power, max_size) = ((x, y), subgrid_power, size)

print max_cell_3
print max_cell, max_size
