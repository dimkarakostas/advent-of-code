def parse_commands(lines):
    commands = []
    for l in lines:
        c, offset = l.split()
        commands.append([c, int(offset)])
    return commands

def run_command(command, idx, acc):
    c, offset = command
    if c == 'acc':
        acc += offset
        idx += 1
    elif c == 'jmp':
        idx += offset
    elif c == 'nop':
        idx += 1
    return idx, acc

def run_program(commands):
    terminated, visited = True, [False for _ in commands]
    acc, idx = 0, 0
    while idx < len(commands):
        if visited[idx]:
            terminated = False
            break
        visited[idx] = True
        idx, acc = run_command(commands[idx], idx, acc)
    return acc, terminated
