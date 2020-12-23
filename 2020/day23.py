from collections import deque

problem_input = '463528179'

inp = deque([int(i) for i in problem_input])

curr = inp[0]
for move in range(100):
    picked = []
    for _ in range(3):
        picked.append(inp[(inp.index(curr) + 1) % len(inp)])
        inp.remove(picked[-1])

    dest = curr - 1
    while dest not in inp:
        dest -= 1
        if dest <= 0:
            dest = max(inp)

    if inp[-1] == dest:
        for i in range(3):
            inp.append(picked[i])
    else:
        dest_idx = inp.index(dest)
        for i in range(2, -1, -1):
            inp.insert(dest_idx+1, picked[i])

    curr = inp[(inp.index(curr) + 1) % len(inp)]

outp = []
idx = inp.index(1) + 1
for i in range(len(inp) - 1):
    outp.append(str(inp[(idx + i) % len(inp)]))
print('Part 1:', ''.join(outp))



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

inp = list([int(i) for i in problem_input])

nodes = [Node(i) for i in range(1000001)]

for idx, item in enumerate(inp[:-1]):
    nodes[item].next = nodes[inp[idx + 1]]

nodes[inp[-1]].next = nodes[max(inp) + 1]

for item in range(max(inp)+1, len(nodes)-1):
    nodes[item].next = nodes[item+1]

nodes[len(nodes)-1].next = nodes[inp[0]]

curr = nodes[inp[0]]
for _ in range(10000000):
    picked = [curr.next, curr.next.next, curr.next.next.next]
    picked_vals = {i.val for i in picked}

    curr.next = picked[-1].next

    dest = curr.val - 1
    while dest in picked_vals or dest == 0:
        dest -= 1
        if dest <= 0:
            dest = len(nodes) - 1

    picked[-1].next = nodes[dest].next
    nodes[dest].next = picked[0]

    curr = curr.next

print('Part 2:', nodes[1].next.val * nodes[1].next.next.val)
