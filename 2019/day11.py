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


def run(flag):
    program = [int(i) for i in open('input11').readlines()[0].split(',')]
    p = Program(program[:])

    x, y = grid_size / 2, grid_size / 2
    painted_panels, white_panels, direction = set(), set(), '^'
    if flag:
        white_panels.add((x, y))

    while not p.halted:
        panel_color = 1 if (x, y) in white_panels else 0
        p.run([panel_color])
        color, steer = p.outputs[-2], p.outputs[-1]
        if color == 1:
            white_panels.add((x, y))
        elif (x, y) in white_panels:
            white_panels.remove((x, y))
        painted_panels.add((x, y))

        if (direction == '^' and steer == 0) or (direction == 'v' and steer == 1):
            direction = '<'
            x, y = x, y - 1
        elif (direction == '^' and steer == 1) or (direction == 'v' and steer == 0):
            direction = '>'
            x, y = x, y + 1
        elif (direction == '>' and steer == 1) or (direction == '<' and steer == 0):
            direction = 'v'
            x, y = x + 1, y
        elif (direction == '>' and steer == 0) or (direction == '<' and steer == 1):
            direction = '^'
            x, y = x - 1, y
    return painted_panels, white_panels

grid_size = 90

print 'Part 1:', len(run(0)[0])
print 'Part 2:'
white_panels = run(1)[1]
for x in range(grid_size):
    ln = ['#' if (x, y) in white_panels else '.' for y in range(grid_size)]
    print ''.join(ln)
