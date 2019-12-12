from fractions import gcd

moons = [[int(c.split('=')[-1]) for c in line.strip()[:-1].split(',')] + [0, 0, 0] for line in open('input12').readlines()]

reached_states = [set(), set(), set(), {}, {}, {}]
periods = [0, 0, 0, False, False, False]
t = 0
flags = [False, False]
while not all(flags):
    for m1 in moons:
        for m2 in moons:
            for i in range(3):
                m1[i + 3] += 1 if m2[i] > m1[i] else -1 if m2[i] < m1[i] else 0
    for m in moons:
        for i in range(3):
            m[i] += m[i + 3]

    t += 1
    if t == 1000:
        energy = sum([sum([abs(i) for i in m[:3]]) * sum([abs(i) for i in m[3:]]) for m in moons])
        print 'Part 1:', energy
        flags[0] = True

    for s in range(3):
        state = tuple([(m[s], m[s + 3]) for m in moons])
        if not periods[s + 3]:
            if state in reached_states[s]:
                periods[s] = t - reached_states[s + 3][state]
                periods[s + 3] = True
            else:
                reached_states[s].add(state)
                reached_states[s + 3][state] = t
    if all(periods[3:]):
        period = periods[0]
        for p in periods[1:3]:
            period = period * p / gcd(period, p)
        print 'Part 2:', period
        flags[1] = True
