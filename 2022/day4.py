full_overlaps = []
overlaps = []
with open('input4') as f:
    for line in f.readlines():
        pairs = line.strip().split(',')
        [start_1, stop_1] = [int(i) for i in pairs[0].split('-')]
        [start_2, stop_2] = [int(i) for i in pairs[1].split('-')]

        if (start_1 <= start_2 and stop_1 >= stop_2) or (start_2 <= start_1 and stop_2 >= stop_1):
            full_overlaps.append(pairs)

        if any([
            start_1 in range(start_2, stop_2+1),
            stop_1 in range(start_2, stop_2+1),
            start_2 in range(start_1, stop_1+1),
            stop_2 in range(start_1, stop_1+1),
        ]):
            overlaps.append(pairs)

print('Part 1:', len(full_overlaps))
print('Part 2:', len(overlaps))
