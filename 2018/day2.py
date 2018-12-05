import re


with open('input2', 'r') as f:
    lst = [i.strip() for i in f.readlines()]

found = [0, 0]
for word in lst:
    flags = [False, False]
    for letter in word:
        length = len([m.start() for m in re.finditer(letter, word)])
        if length == 2 and not flags[0]:
            flags[0] = True
            found[0] += 1
        elif length == 3 and not flags[1]:
            flags[1] = True
            found[1] += 1
        if all(flags):
            break

print 'Part 1:', found[0] * found[1]

for idx in range(len(lst)):
    word = lst[idx]
    for comp_word in lst[idx + 1:]:
        flag = 0
        indices = []
        for i, _ in enumerate(word):
            if word[i] != comp_word[i]:
                indices.append(i)
                flag += 1
                if flag > 1:
                    break
        if flag == 1:
            print 'Part 2:', word[:indices[0]] + word[indices[0] + 1:]
            break
    if flag == 1:
        break
