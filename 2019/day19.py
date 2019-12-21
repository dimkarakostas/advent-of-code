def run(memory, inputs):
    halted, outputs, idx, rel_base = False, [], 0, 0
    used_inputs = 0
    while idx < len(memory):
        instruction = str(memory[idx])
        opcode, modes = int(instruction[-2:]), instruction[:-2][::-1] + 3 * '0'
        idx += 1
        if opcode in (1, 2, 5, 6, 7, 8):  # Two params
            ins = []
            for i in range(2):
                param = memory[idx + i]
                if modes[i] == '0':
                    if param > len(memory) - 1:
                        memory += [0 for _ in range(param)]
                    ins.append(memory[param])
                elif modes[i] == '1':
                    ins.append(param)
                elif modes[i] == '2':
                    if param + rel_base > len(memory) - 1:
                        memory += [0 for _ in range(param + rel_base)]
                    ins.append(memory[param + rel_base])
            if opcode in (1, 2, 7, 8):  # Two params, one output
                assert modes[2] in ('0', '2'), 'Invalid write'
                out = memory[idx + 2]
                if modes[2] == '2':
                    out += rel_base
                if out > len(memory) - 1:
                    memory += [0 for _ in range(out)]
                if opcode in (1, 2):
                    memory[out] = ins[0] + ins[1] if opcode == 1 else ins[0] * ins[1]
                else:
                    if opcode == 7:
                        memory[out] = 1 if ins[0] < ins[1] else 0
                    else:
                        memory[out] = 1 if ins[0] == ins[1] else 0
                idx += 3
            elif opcode in (5, 6):  # Two params, no output
                if any([
                    opcode == 5 and ins[0] != 0,
                    opcode == 6 and ins[0] == 0,
                ]):
                    idx = ins[1]
                else:
                    idx += 2
        elif opcode in (3, 4, 9):  # Single param
            param = memory[idx]
            if param + rel_base > len(memory) - 1:
                memory += [0 for _ in range(param + rel_base)]
            if opcode == 3:
                assert modes[0] in ('0', '2'), 'Invalid write'
                if used_inputs < len(inputs):
                    inp = inputs[used_inputs]
                    used_inputs += 1
                    if modes[0] == '0':
                        memory[param] = inp
                    elif modes[0] == '2':
                        memory[param + rel_base] = inp
                else:
                    idx -= 1
                    return used_inputs
            elif opcode == 4:  # Single input, one output
                if modes[0] == '0':
                    out = memory[param]
                elif modes[0] == '1':
                    out = param
                elif modes[0] == '2':
                    out = memory[param + rel_base]
                outputs.append(out)
            elif opcode == 9:
                if modes[0] == '0':
                    rel_base += memory[param]
                elif modes[0] == '1':
                    rel_base += param
                elif modes[0] == '2':
                    rel_base += memory[param + rel_base]
            idx += 1
        elif opcode in (99, ):  # No param
            halted = True
            break
        else:
            assert False, 'Unknown opcode'
    assert halted, 'Exit without halting'
    return outputs


program = [int(i) for i in open('input19').readlines()[0].split(',')]

SQUARE_SIZE = 100

grid = [['#']]
x_start = 0
affected_points = set([(0, 0)])
found = False
while not found:
    if grid[x_start][-1] == '.':
        x_start += 1

    for ln in grid:
        ln.append('.')
    grid.append(['.' for _ in range(len(grid[0]))])

    y = len(grid) - 1
    entered_beam = False
    for x in range(x_start, len(grid)):
        if run(program[:], [x, y])[-1] == 1:
            entered_beam = True
            affected_points.add((x, y))
            grid[x][y] = '#'
        else:
            if entered_beam:
                break
    if len(grid) == 50:
        print 'Part 1:', len(affected_points)

    for (x, y) in affected_points:
        try:
            if grid[x + SQUARE_SIZE - 1][y] == '#' and grid[x][y + SQUARE_SIZE - 1] == '#':
                found = (x, y)
        except IndexError:
            pass
print 'Part 2:', found[0] * 10000 + found[1]
