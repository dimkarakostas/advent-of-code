nums = sorted([int(i.strip()) for i in open('input1').readlines()])

flag1, flag2 = True, True
for n1 in nums:
    if not flag1 and not flag2:
        break
    for n2 in nums:
        if n1 + n2 == 2020 and flag1:
            print('Part 1:', n1 * n2)
            flag1 = False
        for n3 in nums:
            if n1 + n2 + n3 == 2020 and flag2:
                print('Part 2:', n1 * n2 * n3)
                flag2 = False
