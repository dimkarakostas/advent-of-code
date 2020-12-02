import re

lines = open('input2').readlines()

rg = r'(\d+)-(\d+) (\w): (\w+)'
valid1, valid2 = 0, 0
for l in lines:
    m = re.match(rg, l)
    low, high, char, pwd = m.groups()
    low, high = int(low), int(high)

    valid1 += pwd.count(char) in range(low, high + 1)
    valid2 += (pwd[low - 1] == char) != (pwd[high - 1] == char)

print('Part1:', valid1)
print('Part2:', valid2)
