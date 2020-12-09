from collections import defaultdict

lines = [int(l.strip()) for l in open('input9').readlines()]

offset = 25
precomputed = defaultdict(list)
for i in range(len(lines) - offset):
    for j in range(i+1, i+offset):
        precomputed[i].append(lines[i] + lines[j])

for idx, candidate in enumerate(lines[offset:], start=offset):
    if candidate not in set().union(*[set(precomputed[j][:idx-j]) for j in range(idx-offset, idx)]):
        break
print('Part 1:', candidate)

i, j = 0, 1
while sum(lines[i:j]) != candidate:
    while sum(lines[i:j]) < candidate:
        j += 1
    while sum(lines[i:j]) > candidate:
        i += 1
print('Part 2:', max(lines[i:j]) + min(lines[i:j]))
