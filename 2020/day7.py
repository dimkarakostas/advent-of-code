import re
from collections import defaultdict

lines = [l.strip() for l in open('input7').readlines()]

rg = r'((\d)?( )?(\w+ \w+) bags?)'
contains, is_contained_in = defaultdict(set), defaultdict(set)
for l in lines:
    matched = re.findall(rg, l)
    outer = matched[0][3]
    if 'no other' not in l:
        for b in matched[1:]:
            inner, num = b[3], int(b[1])
            contains[outer].add((inner, num))
            is_contained_in[inner].add(outer)

bag = 'shiny gold'

explored, horizon = set(), set([bag])
while len(horizon) > 0:
    item = horizon.pop()
    explored.add(item)
    horizon = horizon.union(is_contained_in[item] - explored)
print('Part 1:', len(explored - set([bag])))

def recur(bag):
    return sum([
        num * (1 + recur(item)) for item, num in contains[bag]
    ])

print('Part 2:', recur(bag))
