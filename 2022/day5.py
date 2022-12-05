from collections import defaultdict
from string import ascii_uppercase
import copy

input_file = 'input5'

move_idx = -1
original_stacks = defaultdict(list)
with open(input_file) as f:
    for idx, line in enumerate(f.readlines()):
        for (stack_no, item_idx) in enumerate(range(1, len(line), 4)):
            if line[item_idx] in ascii_uppercase: 
                original_stacks[stack_no + 1].insert(0, line[item_idx])
        if '[' not in line:
            move_idx = idx + 2
            break

moves = []
with open(input_file) as f:
    for line in f.readlines()[move_idx:]:
        _, boxes, _, source, _, dest = line.strip().split()
        moves.append([int(boxes), int(source), int(dest)])

stacks = copy.deepcopy(original_stacks)
for (boxes, source, dest) in moves:
    for _ in range(boxes):
        item = stacks[source].pop()
        stacks[dest].append(item)

crates = ''
for (_, stack) in sorted(stacks.items(), key=lambda x: x[0]):
    crates += stack[-1]
print('Part 1:', crates)


stacks = copy.deepcopy(original_stacks)
for (boxes, source, dest) in moves:
    stacks[dest] += stacks[source][-1*boxes:]
    stacks[source] = stacks[source][:-1*boxes]

crates = ''
for (_, stack) in sorted(stacks.items(), key=lambda x: x[0]):
    crates += stack[-1]
print('Part 2:', crates)
