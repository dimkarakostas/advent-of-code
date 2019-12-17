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


program = [int(i) for i in open('input17').readlines()[0].split(',')]
p = Program(program[:])
p.run([])

output = ''.join([chr(int(i)) for i in p.outputs[:-2]])
grid = [['.'] + list(ln) + ['.'] for ln in output.split('\n')]
empty_line = ['.' for _ in range(len(grid[0]))]
grid = [empty_line] + grid + [empty_line]
for ln in grid:
    print ''.join(ln)

intersections = []
for x, ln in enumerate(grid):
    for y, elem in enumerate(ln):
        if elem == '#' and all([
            grid[x - 1][y] == '#',
            grid[x + 1][y] == '#',
            grid[x][y - 1] == '#',
            grid[x][y + 1] == '#'
        ]):
            intersections.append((x - 1, y - 1))
print 'Part 1:', sum([i[0] * i[1] for i in intersections])

# MANUALLY FOUND PATH:
# L,6,R,12,L,6,L,8,L,8,L,6,R,12,L,6,L,8,L,8,L,6,R,12,R,8,L,8,L,4,L,4,L,6,L,6,R,12,R,8,L,8,L,6,R,12,L,6,L,8,L,8,L,4,L,4,L,6,L,6,R,12,R,8,L,8,L,4,L,4,L,6,L,6,R,12,L,6,L,8,L,8

p = Program(program[:])
p.memory[0] = 2
main = 'A,A,B,C,B,A,C,B,C,A\n'
A = 'L,6,R,12,L,6,L,8,L,8\n'
B = 'L,6,R,12,R,8,L,8\n'
C = 'L,4,L,4,L,6\n'
feed = 'n\n'
p.run([ord(j) for j in ''.join([main, A, B, C, feed])])
print 'Part 2:', p.outputs[-1]
