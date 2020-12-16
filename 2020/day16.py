import re
from functools import reduce
import operator

lines = [l.strip() for l in open('input16').readlines()]

rg = r'^(\w+\s?\w+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$'

rules = {}
for idx, l in enumerate(lines):
    if l == '':
        break

    groups = re.match(rg, l).groups()
    field = groups[0]
    start_1, end_1, start_2, end_2 = (int(i) for i in groups[1:])

    rules[field] = [(start_1, end_1), (start_2, end_2)]


sorted_ranges = sorted([item for val in rules.values() for item in val])
union_range = []
for start, end in sorted_ranges:
    if union_range and union_range[-1][1] >= start:
        union_range[-1][1] = max(union_range[-1][1], end)
    else:
        union_range.append([start, end])

idx += 2
my_ticket = [int(i) for i in lines[idx].split(',')]

idx += 3
error_rate = 0
nearby_tickets = []
for l in lines[idx:]:
    ticket = [int(i) for i in l.split(',')]
    valid = True
    for val in ticket:
        if not any([
            val in range(start, end + 1) for (start, end) in union_range
        ]):
            error_rate += val
            valid = False
            break
    if valid:
        nearby_tickets.append(ticket)

print('Part 1:', error_rate)


fields = [set(rules.keys()) for _ in rules.keys()]
for ticket in nearby_tickets:
    for idx, val in enumerate(ticket):
        applicable_rules = set()
        for rule_name in rules.keys():
            if any([
                val in range(start, end + 1) for (start, end) in rules[rule_name]
            ]):
                applicable_rules.add(rule_name)
        fields[idx] = fields[idx].intersection(applicable_rules)

single_element_fields = set()
while any([len(item) > 1 for item in fields]):
    for candidate in fields:
        if len(candidate) > 1:
            candidate -= single_element_fields
        else:
            single_element_fields.add(next(iter(candidate)))

output = reduce(
    operator.mul,
    [my_ticket[idx] for idx, item in enumerate(fields) if 'departure' in next(iter(item))]
)
print('Part 2:', output)
