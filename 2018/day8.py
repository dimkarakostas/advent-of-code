with open('input8') as f:
    data = [int(i) for i in f.read().split()]


def explore(root, metasum):
    children = data[root]
    metamount = data[root + 1]
    metaposition = root + 2
    children_values = []
    if children:
        for _ in range(children):
            metasum, metaposition, value = explore(metaposition, metasum)
            children_values.append(value)
        value = 0
        for meta in data[metaposition:metaposition + metamount]:
            try:
                value += children_values[meta - 1]
            except IndexError:
                pass
    else:
        value = sum(data[metaposition:metaposition + metamount])
    metasum += sum(data[metaposition:metaposition + metamount])
    return metasum, metaposition + metamount, value


explored = explore(0, 0)
print 'Part 1:', explored[0]
print 'Part 2:', explored[2]
