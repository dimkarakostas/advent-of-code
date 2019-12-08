from itertools import permutations


class Amplifier:
    def __init__(self, program, phase):
        self.program = program
        self.halted = False
        self.outputs, self.idx = [], 0
        self.run([phase])

    def run(self, inputs):
        used_inputs = 0
        while self.idx < len(self.program):
            instruction = str(self.program[self.idx])
            opcode, modes = int(instruction[-2:]), instruction[:-2][::-1] + 3 * '0'
            self.idx += 1
            if opcode == 99:
                self.halted = True
                return 0
            elif opcode in (1, 2, 5, 6, 7, 8):  # Two params
                in1 = self.program[self.program[self.idx]] if modes[0] == '0' else self.program[self.idx]
                in2 = self.program[self.program[self.idx + 1]] if modes[1] == '0' else self.program[self.idx + 1]
                if opcode in (1, 2, 7, 8):  # Two params, one output
                    assert modes[2] == '0', 'Invalid write'
                    out = self.program[self.idx + 2]
                    if opcode in (1, 2):
                        self.program[out] = in1 + in2 if opcode == 1 else in1 * in2
                    else:
                        if opcode == 7:
                            self.program[out] = 1 if in1 < in2 else 0
                        else:
                            self.program[out] = 1 if in1 == in2 else 0
                    self.idx += 3
                elif opcode in (5, 6):  # Two params, no output
                    if any([
                        opcode == 5 and in1 != 0,
                        opcode == 6 and in1 == 0,
                    ]):
                        self.idx = in2
                    else:
                        self.idx += 2
            elif opcode in (3, 4):  # Single param
                param = self.program[self.idx]
                if opcode == 3:
                    assert modes[0] == '0', 'Invalid write'
                    if used_inputs < len(inputs):
                        self.program[param] = inputs[used_inputs]
                        used_inputs += 1
                        self.idx += 1
                    else:
                        self.idx -= 1
                        return used_inputs
                elif opcode == 4:  # Single input, one output
                    out = self.program[param] if modes[0] == '0' else param
                    self.idx += 1
                    self.outputs.append(out)
            else:
                assert False, 'Unknown opcode'
        assert False, 'Exit without halting'


program = [int(i) for i in open('input7').readlines()[0].split(',')]

phases = permutations(range(5), 5)
max_signal = 0
for p in phases:
    amps = [Amplifier(program[:], p[i]) for i in range(5)]
    amps[0].run([0])
    for i in range(1, 5):
        amps[i].run(amps[i - 1].outputs[-1:])
    if amps[4].outputs[-1] > max_signal:
        max_signal = amps[4].outputs[-1]
print 'Part 1:', max_signal

phases = permutations(range(5, 10), 5)
max_signal = 0
max_phase = []
for p in phases:
    amps = [Amplifier(program[:], p[i]) for i in range(5)]
    amps[0].run([0])
    used_inputs = [0 for _ in range(5)]
    while not any([amp.halted for amp in amps]):
        for i in range(5):
            used_inputs[i] += amps[i].run(amps[i - 1].outputs[used_inputs[i]:])
    if amps[4].outputs[-1] > max_signal:
        max_signal = amps[4].outputs[-1]
print 'Part 2:', max_signal
