def fuel(m):
    return (m / 3) - 2

def extra_fuel(m):
    fuels = 0
    while fuel(m) > 0:
        m = fuel(m)
        fuels += m
    return fuels

masses = [int(l) for l in open('input1').readlines()]
print 'Part 1:', sum([fuel(m) for m in masses])
print 'Part 2:', sum([extra_fuel(m) for m in masses])
