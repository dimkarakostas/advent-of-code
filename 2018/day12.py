rounds = 50000000000
pad = 400

with open('input12', 'r') as f:
    fl = f.read()
    state = (pad * '.') + fl.split('\n')[0].split()[2] + (pad * '.')
    rules = []
    for line in fl.split('\n')[2:-1]:
        sline = line.split()
        if sline[2] == '#':
            rules.append(sline[0])

equilibrium_flag = 0
hashcount = state.count('#')
for r in xrange(1, rounds + 1):
    new_state = ['.' for _ in range(len(state))]
    for idx in range(2, len(state) - 2):
        if state[idx - 2:idx + 3] in rules:
            new_state[idx] = '#'
    new_state = ''.join(new_state)
    if equilibrium_flag == 5:
        shift = new_state.find('#') - state.find('#')
        print 'Part 2:', sum([(pos - pad) + shift * (rounds - r) for pos, ch in enumerate(new_state) if ch == '#'])
        break
    state = new_state
    if r == 20:
        print 'Part 1:', sum([pos - pad for pos, ch in enumerate(state) if ch == '#'])
    equilibrium_flag = equilibrium_flag + 1 if hashcount == state.count('#') else 0
    hashcount = state.count('#')
