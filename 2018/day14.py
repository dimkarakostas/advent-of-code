def subfinder(mylist, pattern):
    for i in xrange(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i + len(pattern)] == pattern:
            return i
    return -1


INPUT = 330121
INPUT_LIST = [int(i) for i in list(str(INPUT))]

elf1 = 0
elf2 = 1
recipes = [3, 7]
flags = [False, False]
while not all(flags):
    score = recipes[elf1] + recipes[elf2]
    digits = [int(i) for i in list(str(score))]
    recipes += digits
    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
    if not flags[0] and len(recipes) > (INPUT + 10):
        print 'First part:', ''.join([str(i) for i in recipes[INPUT:INPUT + 10]])
        flags[0] = True
    if len(recipes) % 100000 == 0:
        found = subfinder(recipes, INPUT_LIST)
        if found > 0:
            print 'Second part:', found
            flags[1] = True
