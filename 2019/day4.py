start, end = 206938, 679128

part1, part2 = 0, 0
for i in range(start, end + 1):
    d = [int(c) for c in str(i)]
    if sorted(d) == d and any([d.count(i) >= 2 for i in d]):
        part1 += 1
        if any([d.count(i) == 2 for i in d]):
            part2 += 1

print 'Part 1:', part1
print 'Part 2:', part2
