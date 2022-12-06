with open('input6') as f:
    signal = f.read().strip()

for idx in range(3, len(signal)):
    if len(set(signal[idx-3:idx+1])) == 4:
        print('Part 1:', idx+1)
        break

for idx in range(13, len(signal)):
    if len(set(signal[idx-13:idx+1])) == 14:
        print('Part 2:', idx+1)
        break
