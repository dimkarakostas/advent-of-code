lines = [l.strip() for l in open('input6').readlines()]

groups = [[]]
for l in lines:
    if l == '':
        groups.append([])
    else:
        groups[-1].append(set(l))

total_1 = sum([len(set.union(*g)) for g in groups])
print('Part 1:', total_1)

total_2 = sum([len(set.intersection(*g)) for g in groups])
print('Part 2:', total_2)
