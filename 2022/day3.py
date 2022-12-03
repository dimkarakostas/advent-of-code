from string import ascii_lowercase, ascii_uppercase

priorities = ascii_lowercase + ascii_uppercase

output = 0
with open('input3') as f:
    for line in f.readlines():
        set1 = set(line.strip()[:int(len(line)/2)])
        set2 = set(line.strip()[int(len(line)/2):])
        common = set1.intersection(set2).pop()
        output += priorities.index(common) + 1

print('Part 1:', output)

output = 0
with open('input3') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        set1 = set(lines[i].strip())
        set2 = set(lines[i+1].strip())
        set3 = set(lines[i+2].strip())
        common = set1.intersection(set2).intersection(set3).pop()
        output += priorities.index(common) + 1

print('Part 2:', output)
