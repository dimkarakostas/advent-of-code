choices = ['A', 'B', 'C']

points = 0
with open('input2') as f:
    for line in f.readlines():
        opponent, me = line.strip().split()
        me = chr(ord(me) - (ord('X') - ord('A')))

        points += choices.index(me) + 1

        if me == opponent:
            points += 3
        elif choices[choices.index(me) - 1] == opponent:
            points += 6

print('Part 1:', points)

points = 0
with open('input2') as f:
    for line in f.readlines():
        opponent, me = line.strip().split()

        if me == 'Y':
            points += choices.index(opponent) + 1 + 3
        elif me == 'X':
            points += choices.index(choices[choices.index(opponent) - 1]) + 1
        else:
            points += choices.index(choices[choices.index(opponent) - 2]) + 1 + 6

print('Part 2:', points)
