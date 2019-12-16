class Program:
    def __init__(self, memory):
        self.memory = memory
        self.halted, self.outputs, self.idx, self.rel_base = False, [], 0, 0

    def run(self, inputs):
        used_inputs = 0
        while self.idx < len(self.memory):
            instruction = str(self.memory[self.idx])
            opcode, modes = int(instruction[-2:]), instruction[:-2][::-1] + 3 * '0'
            self.idx += 1
            if opcode in (1, 2, 5, 6, 7, 8):  # Two params
                ins = []
                for i in range(2):
                    param = self.memory[self.idx + i]
                    if modes[i] == '0':
                        if param > len(self.memory) - 1:
                            self.memory += [0 for _ in range(param)]
                        ins.append(self.memory[param])
                    elif modes[i] == '1':
                        ins.append(param)
                    elif modes[i] == '2':
                        if param + self.rel_base > len(self.memory) - 1:
                            self.memory += [0 for _ in range(param + self.rel_base)]
                        ins.append(self.memory[param + self.rel_base])
                if opcode in (1, 2, 7, 8):  # Two params, one output
                    assert modes[2] in ('0', '2'), 'Invalid write'
                    out = self.memory[self.idx + 2]
                    if modes[2] == '2':
                        out += self.rel_base
                    if out > len(self.memory) - 1:
                        self.memory += [0 for _ in range(out)]
                    if opcode in (1, 2):
                        self.memory[out] = ins[0] + ins[1] if opcode == 1 else ins[0] * ins[1]
                    else:
                        if opcode == 7:
                            self.memory[out] = 1 if ins[0] < ins[1] else 0
                        else:
                            self.memory[out] = 1 if ins[0] == ins[1] else 0
                    self.idx += 3
                elif opcode in (5, 6):  # Two params, no output
                    if any([
                        opcode == 5 and ins[0] != 0,
                        opcode == 6 and ins[0] == 0,
                    ]):
                        self.idx = ins[1]
                    else:
                        self.idx += 2
            elif opcode in (3, 4, 9):  # Single param
                param = self.memory[self.idx]
                if param + self.rel_base > len(self.memory) - 1:
                    self.memory += [0 for _ in range(param + self.rel_base)]
                if opcode == 3:
                    assert modes[0] in ('0', '2'), 'Invalid write'
                    if used_inputs < len(inputs):
                        inp = inputs[used_inputs]
                        used_inputs += 1
                        if modes[0] == '0':
                            self.memory[param] = inp
                        elif modes[0] == '2':
                            self.memory[param + self.rel_base] = inp
                    else:
                        self.idx -= 1
                        return used_inputs
                elif opcode == 4:  # Single input, one output
                    if modes[0] == '0':
                        out = self.memory[param]
                    elif modes[0] == '1':
                        out = param
                    elif modes[0] == '2':
                        out = self.memory[param + self.rel_base]
                    self.outputs.append(out)
                elif opcode == 9:
                    if modes[0] == '0':
                        self.rel_base += self.memory[param]
                    elif modes[0] == '1':
                        self.rel_base += param
                    elif modes[0] == '2':
                        self.rel_base += self.memory[param + self.rel_base]
                self.idx += 1
            elif opcode in (99, ):  # No param
                self.halted = True
                break
            else:
                assert False, 'Unknown opcode'
        assert self.halted, 'Exit without halting'

class _Getch:
    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

getch = _Getch()

program = [int(i) for i in open('input15').readlines()[0].split(',')]
p = Program(program[:])

grid_size = 70
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
d_x, d_y = grid_size / 2, grid_size / 2
init_x, init_y = d_x, d_y
o_x, o_y, found = -1, -1, False

# STEP 1: Explore grid

moves = []
while True:
    grid[init_x][init_y] = 'o'
    grid[d_x][d_y] = '@'
    if found:
        grid[o_x][o_y] = '$'
    for ln in grid:
        print ''.join(ln)
    move = getch()
    moves.append(move)
    if move == 'a':
        s_x, s_y = d_x, d_y - 1
        inp = 1
    elif move == 'd':
        s_x, s_y = d_x, d_y + 1
        inp = 2
    elif move == 'w':
        s_x, s_y = d_x - 1, d_y
        inp = 3
    elif move == 's':
        s_x, s_y = d_x + 1, d_y
        inp = 4
    elif move == 'p':
        break
    p.run([inp])
    if p.outputs[-1] == 0:
        grid[s_x][s_y] = '#'
    elif p.outputs[-1] in (1, 2):
        grid[d_x][d_y] = ' '
        d_x, d_y = s_x, s_y
        if p.outputs[-1] == 2:
            found = True
open('moves', 'w').write(''.join(moves))

# STEP 2: BFS to fill grid with oxygen and find shortest path
empty_cells = set()
for x, ln in enumerate(grid):
    for y, c in enumerate(ln):
        if c not in ('#', '.'):
            empty_cells.add((x, y))
visited, horizon = set(), set()
horizon.add((o_x, o_y))
mins = 0
while len(visited) < len(empty_cells):
    if ((init_x, init_y)) in horizon:
        print 'Part 1:', mins
    mins += 1
    new_horizon = set()
    for (c_x, c_y) in horizon:
        visited.add((c_x, c_y))
        for i in (-1, 1):
            if grid[c_x + i][c_y] not in ('#', '.') and (c_x + i, c_y) not in visited.union(horizon):
                new_horizon.add((c_x + i, c_y))
            if grid[c_x][c_y + i] not in ('#', '.') and (c_x, c_y + i) not in visited.union(horizon):
                new_horizon.add((c_x, c_y + i))
    horizon = (horizon.union(new_horizon)).difference(visited)
print 'Part 2:', mins - 1
