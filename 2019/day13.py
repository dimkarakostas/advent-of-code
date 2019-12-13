class Program:
    def __init__(self, memory):
        self.memory = memory
        self.halted, self.outputs, self.idx, self.rel_base = False, [], 0, 0
        self.memory[0] = 2

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


program = [int(i) for i in open('input13').readlines()[0].split(',')]
p = Program(program[:])
p.run([])
instructions = []
for i in range(0, len(p.outputs), 3):
    instructions.append(p.outputs[i:i + 3])
blocks = [i for i in instructions if i[2] == 2]
print 'Part 1:', len(blocks)

move = raw_input('If you want to play game input 1 (else AI is used):')
PLAY_GAME_FLAG = True if move == '1' else False

if PLAY_GAME_FLAG:
    print
    print '~~~~ Use (0, 1, 2) to move (center, left, right) ~~~~'
    print
    grid = [[' ' for _ in range(38)] for _ in range(21)]
    for i in instructions:
        if i[2] != 0:
            grid[i[1]][i[0]] = i[2]

paddle = [i for i in instructions if i[2] == 3][0]
ball = [i for i in instructions if i[2] == 4][0]

scores = [i[2] for i in instructions if (i[0], i[1]) == (-1, 0)]
while len(scores) < len(blocks) + 1:
    if PLAY_GAME_FLAG:
        for l in grid:
            print ''.join([str(i) for i in l])
        try:
            move = int(raw_input('Input:'))
        except ValueError:
            move = 0
            pass
        inp = -1 if move == 1 else 1 if move == 2 else 0
    else:
        inp = -1 if paddle[0] > ball[0] else 1 if paddle[0] < ball[0] else 0

    p.run([inp])

    if PLAY_GAME_FLAG:
        grid[paddle[1]][paddle[0]] = ' '
        grid[ball[1]][ball[0]] = ' '

    instructions = []
    for i in range(0, len(p.outputs), 3):
        instructions.append(p.outputs[i:i + 3])
    ball = [i for i in instructions if i[2] == 4][-1]
    paddle = [i for i in instructions if i[2] == 3][-1]

    if PLAY_GAME_FLAG:
        grid[paddle[1]][paddle[0]] = 3
        grid[ball[1]][ball[0]] = 4

    scores = [i[2] for i in instructions if (i[0], i[1]) == (-1, 0)]
print 'Part 2:', scores[-1]
