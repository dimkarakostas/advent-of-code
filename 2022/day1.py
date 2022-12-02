elves = [] 
with open('input1') as f:
    calories = 0
    for line in f.readlines():
        try:
            calories += int(line.strip())
        except ValueError:
            elves.append(calories)
            calories = 0

print('Part 1:', max(elves))
print('Part 2:', sum([
    i for i in sorted(elves, reverse=True)[:3]
]))
