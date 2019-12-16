inp = open('input16').read().strip()
inp = [int(i) for i in inp]
base = [0, 1, 0, -1]

for phase in xrange(1, 101):
    new_inp = []
    for dgt in range(1, len(inp) + 1):
        partial_pos_sum = [sum(inp[i:i + dgt]) for i in range(dgt - 1, len(inp), len(base) * dgt)]
        partial_neg_sum = [-1 * sum(inp[i:i + dgt]) for i in range(dgt * 3 - 1, len(inp), len(base) * dgt)]
        new_inp.append(int(str(sum(partial_pos_sum) + sum(partial_neg_sum))[-1]))
    inp = new_inp
print 'Part 1:', ''.join([str(i) for i in inp])[:8]

inp = open('input16').read().strip()
offset = int(inp[:7])
inp = 10000 * [int(i) for i in inp]

if offset < len(inp) / 2:
    print 'Offset not large enough, solution does not apply.'
else:
    inp = list(reversed(inp[offset:]))
    for _ in range(100):
        partial_sum = 0
        new_inp = []
        for i in range(len(inp)):
            partial_sum += inp[i]
            new_inp.append(int(str(partial_sum)[-1]))
        inp = new_inp
    print 'Part 2:', ''.join(str(i) for i in inp[-1:-9:-1])
