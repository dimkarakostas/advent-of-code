from program import parse_commands, run_program

lines = [l.strip() for l in open('input8').readlines()]

commands = parse_commands(lines)

acc, _ = run_program(commands)
print('Part 1:', acc)

for idx, (cmd, _) in enumerate(commands):
    if cmd == 'nop':
        commands[idx][0] = 'jmp'
    elif cmd == 'jmp':
        commands[idx][0] = 'nop'
    acc, terminated = run_program(commands)
    if terminated:
        print('Part 2:', acc)
        break
    commands[idx][0] = cmd
