with open('input1', 'r') as f:
    freq_list = [int(i) for i in f.readlines()]

print 'Part 1:', sum(freq_list)

found = False
i = 0
freq = 0
visited_freqs = set([0])
length = len(freq_list)
while not found:
    freq += freq_list[i % length]
    if freq in visited_freqs:
        found = True
        print 'Part 2:', freq
    else:
        visited_freqs.add(freq)
    i += 1
