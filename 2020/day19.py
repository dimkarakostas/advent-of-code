import re

lines = [l.strip() for l in open('input19').readlines()]

rg = r'\s([\d+\s]+)'
rules = {}
for idx, l in enumerate(lines):
    if l == '':
        break
    rule_num, rule = l.split(':')
    if '"' in rule:
        rules[int(rule_num)] = rule[2]
    else:
        grouped = [m.split() for m in re.findall(rg, l)]
        rules[int(rule_num)] = '|'.join([
            ''.join('(%s)' % elem for elem in g) for g in grouped
        ])

def solve(rules):
    rule_zero = rules[0]
    iterations = 0
    while any([char.isdigit() for char in rule_zero]) and iterations < 40:
        iterations += 1
        for r in rules.keys():
            rule_zero = rule_zero.replace('(%d)' % r, '(%s)' % rules[r])

    return [l for l in lines[idx:] if re.compile('^' + rule_zero + '$').match(l)]

print('Part 1:', len(solve(rules)))

rules[8] = '(42)|(42)(8)'
rules[11] = '(42)(31)|(42)(11)(31)'
print('Part 2:', len(solve(rules)))
