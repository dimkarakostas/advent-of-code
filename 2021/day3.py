def get_common_bits(lines, most_common=True):
    common_bits = []
    for bit_idx in range(len(lines[0])):
        bits = [num[bit_idx] for num in lines]
        counts = [bits.count('0'), bits.count('1')]
        if counts[0] == counts[1]:
            common_bits.append('1' if most_common else '0')
        else:
            common_bits.append(str(counts.index(
                max(counts) if most_common else min(counts)
            )))
    return ''.join(common_bits)

def repeated_common(lines, most_common=True):
    elem_set = set(lines)
    bit_idx = 0
    while len(elem_set) > 1:
        common_bits = get_common_bits(list(elem_set), most_common)
        for elem in set(elem_set):
            if elem[bit_idx] != common_bits[bit_idx]:
                elem_set.remove(elem)
        bit_idx += 1
    return elem_set.pop()


lines = [l.strip() for l in open('input3').readlines()]

gamma_digits = get_common_bits(lines)
epsilon_digits = get_common_bits(lines, False)
print('Part 1:', int(gamma_digits, 2) * int(epsilon_digits, 2))

oxy_digits = repeated_common(lines)
co_digits = repeated_common(lines, False)
print('Part 2:', int(oxy_digits, 2) * int(co_digits, 2))
