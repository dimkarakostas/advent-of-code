nums = [2,0,6,12,1,3]

spoken_time = {k: v for v, k in enumerate(nums[:-1])}

last_spoken_num = nums[-1]
turn = len(nums) - 1
while turn < 30000000:
    diff = 0
    if last_spoken_num in spoken_time.keys():
        diff = turn - spoken_time[last_spoken_num]
    spoken_time[last_spoken_num] = turn
    last_spoken_num = diff
    turn += 1

    if turn == 2019:
        print('Part 1:', last_spoken_num)
print('Part 2:', last_spoken_num)
