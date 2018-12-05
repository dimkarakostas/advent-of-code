from string import ascii_lowercase

with open('input5', 'r') as f:
    in_polymer = f.read().strip()

letter_distances = [ord('a') - ord('A'), ord('A') - ord('a')]


def collapse_polymer(polymer):
    idx = 0
    while idx < len(polymer) - 1:
        if ord(polymer[idx]) - ord(polymer[idx + 1]) in letter_distances:
            polymer = polymer[:idx] + polymer[idx + 2:]
            if idx > 0:
                idx -= 1
        else:
            idx += 1
    return polymer


print 'Part 1:', len(collapse_polymer(in_polymer))

best_polymer = in_polymer
for letter in ascii_lowercase:
    temp_polymer = in_polymer.replace(letter, '')
    temp_polymer = temp_polymer.replace(chr(ord(letter) - letter_distances[0]), '')
    collapsed = collapse_polymer(temp_polymer)
    if len(collapsed) < len(best_polymer):
        best_polymer = collapsed

print 'Part 2:', len(best_polymer)
