import operator
from collections import defaultdict

with open('input4', 'r') as f:
    events = sorted(f.readlines())

guard_shifts = defaultdict(list)
guard_totals = defaultdict(int)

guard_id = ''
for e in events:
    e = e.split()
    if e[-1] == 'shift':
        guard_id = int(e[3][1:])
    if e[-1] in ['asleep', 'up']:
        guard_shifts[guard_id].append(int(e[1][3:5]))
        if e[-1] == 'up':
            guard_totals[guard_id] += guard_shifts[guard_id][-1] - guard_shifts[guard_id][-2]

max_guard = (0, 0, 0)
guard_mins = {}
for guard_id in guard_shifts:
    guard_mins[guard_id] = [0 for _ in range(60)]
    shifts = guard_shifts[guard_id]
    for idx in range(0, len(shifts), 2):
        start = shifts[idx]
        stop = shifts[idx + 1]
        for m in range(start, stop):
            guard_mins[guard_id][m] += 1
    max_idx = int(guard_mins[guard_id].index(max(guard_mins[guard_id])))
    if guard_mins[guard_id][max_idx] > max_guard[2]:
        max_guard = (guard_id, max_idx, guard_mins[guard_id][max_idx])

guard_id = max(guard_totals.iteritems(), key=operator.itemgetter(1))[0]
print 'Part 1:', guard_id * int(guard_mins[guard_id].index(max(guard_mins[guard_id])))

print 'Part 2:', max_guard[0] * max_guard[1]
