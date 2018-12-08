with open('input7') as f:
    nodes = {}
    for s in f:
        sp = s.split()
        parent = sp[1]
        if parent not in nodes:
            nodes[parent] = {
                'parents': [],
                'children': []
            }

        child = sp[-3]
        if child not in nodes:
            nodes[child] = {
                'parents': [],
                'children': []
            }

        nodes[parent]['children'].append(child)
        nodes[child]['parents'].append(parent)

horizon = set(nodes.keys())
solution = ''
while horizon:
    for idx, current in enumerate(sorted(horizon)):
        found = True
        for n in horizon:
            if current in nodes[n]['children']:
                found = False
                break
        if found:
            solution += current
            horizon.remove(current)
            break
print 'Part 1:', solution

horizon = set(nodes.keys())
working = set()
workers = ['' for _ in range(5)]
seconds = -1
while horizon or working:
    seconds += 1

    finished = set()
    for n in working:
        if seconds - n[1] > 60 + ord(n[0]) - ord('A'):
            finished.add(n)
            workers[workers.index(n[0])] = ''
    working -= finished

    while horizon or working:
        found = False
        for idx, current in enumerate(sorted(horizon)):
            found = True
            for n in horizon | set([w[0] for w in working]):
                if current in nodes[n]['children']:
                    found = False
                    break
            if found:
                break
        if not found or '' not in workers:
            break
        workers[workers.index('')] = current
        working.add((current, seconds))
        horizon.remove(current)

print 'Part 2:', seconds
