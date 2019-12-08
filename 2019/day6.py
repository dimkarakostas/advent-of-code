from collections import defaultdict

with open('input6') as f:
    direct_parents = defaultdict(set)
    ancestors = defaultdict(set)
    for line in f.readlines():
        source, dest = line.strip().split(')')
        ancestors[dest].add(source)
        direct_parents[dest].add(source)
        new_ancestors = set([source])
        for parent in ancestors[source]:
            ancestors[dest].add(parent)
            new_ancestors.add(parent)
        for n in ancestors:
            if dest in ancestors[n]:
                ancestors[n] = ancestors[n].union(new_ancestors)

print 'Part 1:', sum([len(ancestors[s]) for s in ancestors])

you_horizon = direct_parents['YOU']
you_step_dict = defaultdict(int)
for p in you_horizon:
    you_step_dict[p] = 1

san_horizon = direct_parents['SAN']
san_step_dict = defaultdict(int)
for p in san_horizon:
    san_step_dict[p] = 1

while not you_horizon.intersection(san_horizon):
    for n in you_horizon.copy():
        for p in direct_parents[n]:
            you_horizon.add(p)
            if not you_step_dict[p]:
                you_step_dict[p] = you_step_dict[n] + 1
    for n in san_horizon.copy():
        for p in direct_parents[n]:
            san_horizon.add(p)
            if not san_step_dict[p]:
                san_step_dict[p] = san_step_dict[n] + 1

print 'Part 2:', min([san_step_dict[inter] + you_step_dict[inter] - 2 for inter in you_horizon.intersection(san_horizon)])
