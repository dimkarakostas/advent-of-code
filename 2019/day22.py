def shuffle(moves, stack_size):
    stack = range(stack_size)
    for move in moves:
        if move[0] == 'deal' and move[1] == 'into':
            stack.reverse()
        elif move[0] == 'cut':
            idx = int(move[-1])
            stack = stack[idx:] + stack[:idx]
        else:
            idx = int(move[-1])
            new_stack = stack[:]
            for i in range(stack_size):
                new_stack[i * idx % stack_size] = stack[i]
            stack = new_stack
    return stack

def calculate_card(moves, card_idx, stack_size):
    for move in moves:
        if move[0] == 'deal' and move[1] == 'into':
            card_idx = stack_size - card_idx - 1
        elif move[0] == 'cut':
            cut_idx = int(move[-1])
            card_idx = (card_idx - cut_idx) % stack_size
        else:
            card_idx = (card_idx * int(move[-1])) % stack_size
    return card_idx

moves = [ln.strip().split() for ln in open('input22').readlines()]
card, stack_size = 2019, 10007
print 'Part 1:', shuffle(moves, stack_size).index(card)
print 'Part 1:', calculate_card(moves, card, stack_size)

# card, stack_size, repeat = 2020, 119315717514047, 101741582076661
# print 'Part 2:', calculate_card(moves, card, stack_size)
