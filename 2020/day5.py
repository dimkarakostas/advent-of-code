lines = [l.strip() for l in open('input5').readlines()]

def binary_search(bin_top, code):
    bot, top = 0, 2**bin_top - 1
    for idx, val in enumerate(code):
        if val == '-':
            top -= 2 ** (bin_top - 1 - idx)
        elif val == '+':
            bot += 2 ** (bin_top - 1 - idx)
    return top


all_seats = set()
for l in lines:
    row_code = l[:7].replace('F', '-').replace('B', '+')
    row = binary_search(7, row_code)

    col_code = l[7:].replace('L', '-').replace('R', '+')
    col = binary_search(3, col_code)

    all_seats.add(row*8+col)

print('Part 1:', max(all_seats))
for seat_id in range(min(all_seats), max(all_seats)):
    if seat_id not in all_seats:
        print('Part 2:', seat_id)
        break
