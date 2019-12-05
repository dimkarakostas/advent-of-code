def intcode_part1(inst, program_input):
    output = []
    idx = 0
    while idx < len(inst):
        instruction = str(inst[idx])
        opcode, modes = int(instruction[-2:]), instruction[:-2][::-1] + 3 * '0'
        idx += 1
        if opcode == 99:
            break
        elif opcode in (1, 2):  # Two params
            in1 = inst[inst[idx]] if modes[0] == '0' else inst[idx]
            in2 = inst[inst[idx + 1]] if modes[1] == '0' else inst[idx + 1]
            assert modes[2] == '0', 'Invalid write'
            out = inst[idx + 2]
            inst[out] = in1 + in2 if opcode == 1 else in1 * in2
            idx += 3
        elif opcode in (3, 4):  # Single param
            param = inst[idx]
            if opcode == 3:
                assert modes[0] == '0', 'Invalid write'
                inst[param] = program_input
                idx += 1
            elif opcode == 4:  # Single input, one output
                out = inst[param] if modes[0] == '0' else param
                output.append(out)
                idx += 1
        else:
            assert False, 'Unknown opcode'
    return output

def intcode_part2(inst, program_input):
    output = []
    idx = 0
    while idx < len(inst):
        instruction = str(inst[idx])
        opcode, modes = int(instruction[-2:]), instruction[:-2][::-1] + 3 * '0'
        idx += 1
        if opcode == 99:
            break
        elif opcode in (1, 2, 5, 6, 7, 8):  # Two params
            in1 = inst[inst[idx]] if modes[0] == '0' else inst[idx]
            in2 = inst[inst[idx + 1]] if modes[1] == '0' else inst[idx + 1]
            if opcode in (1, 2, 7, 8):  # Two params, one output
                assert modes[2] == '0', 'Invalid write'
                out = inst[idx + 2]
                if opcode in (1, 2):
                    inst[out] = in1 + in2 if opcode == 1 else in1 * in2
                else:
                    if opcode == 7:
                        inst[out] = 1 if in1 < in2 else 0
                    else:
                        inst[out] = 1 if in1 == in2 else 0
                idx += 3
            elif opcode in (5, 6):  # Two params, no output
                if any([
                    opcode == 5 and in1 != 0,
                    opcode == 6 and in1 == 0,
                ]):
                    idx = in2
                else:
                    idx += 2
        elif opcode in (3, 4):  # Single param
            param = inst[idx]
            if opcode == 3:
                assert modes[0] == '0', 'Invalid write'
                inst[param] = program_input
                idx += 1
            elif opcode == 4:  # Single input, one output
                out = inst[param] if modes[0] == '0' else param
                output.append(out)
                idx += 1
        else:
            assert False, 'Unknown opcode'
    return output


inst = [int(i) for i in open('input5').readlines()[0].split(',')]
print 'Part 1:', intcode_part1(inst[:], 1)
print 'Part 2:', intcode_part2(inst[:], 5)
