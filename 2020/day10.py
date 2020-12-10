from collections import defaultdict

lines = sorted([int(l.strip()) for l in open('input10').readlines()])
lines = [0] + lines + [lines[-1] + 3]

diffs = defaultdict(int)
for idx in range(1, len(lines)):
    diffs[lines[idx] - lines[idx-1]] += 1

print('Part 1:', diffs[1]*diffs[3])

# mx, curr = 0, 1
# for idx in range(1, len(lines)):
#     if lines[idx] - lines[idx-1] == 1:
#         curr += 1
#     else:
#         if curr > mx:
#             mx = curr
#         curr = 1
# print('max consecutive numbers:', mx)

consecutive_perms = {
    1: 1,
    2: 1,
    3: 2,
    4: 4,
    5: 7
}

total = 1
i = 0
while i < len(lines):
    j = i + 1
    while j < len(lines) and lines[j] - lines[j-1] == 1:
        j += 1
    total *= consecutive_perms[j-i]
    i = j
print('Part 2:', total)
