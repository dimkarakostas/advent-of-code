lines = [l.strip() for l in open('input25').readlines()]

keys = [int(i) for i in lines]

subject_num = 7
val = 1
count = 0
loops = {}
while len(loops.keys()) < 2:
    count += 1
    val = (val * subject_num) % 20201227
    if val in keys:
        loops[val] = count

val = 1
subject_num = keys[0]
for _ in range(loops[keys[1]]):
    val = (val * subject_num) % 20201227
print('Part 1:', val)
