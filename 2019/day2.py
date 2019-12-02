init = [int(i) for i in open('input2').readlines()[0].split(',')]
for x in xrange(100):
    for y in xrange(100):
        nums = init[:]
        (nums[1], nums[2]) = (x, y)
        for idx in xrange(0, len(nums), 4):
            if nums[idx] == 99:
                if (x, y) == (12, 2):
                    print 'Part 1:', nums[0]
                if nums[0] == 19690720:
                    print 'Part 2:', (100 * nums[1]) + nums[2]
            elif nums[idx] == 1:
                nums[nums[idx + 3]] = nums[nums[idx + 1]] + nums[nums[idx + 2]]
            elif nums[idx] == 2:
                nums[nums[idx + 3]] = nums[nums[idx + 1]] * nums[nums[idx + 2]]
            else:
                break
