import operator

lines = [l.strip().replace(' ', '') for l in open('input18').readlines()]

def parse(inp):
    ops = {
        '+': operator.add,
        '*': operator.mul,
    }

    stack = []
    aggr = None
    for idx, item in enumerate(inp):
        if item.isdigit():
            if type(aggr) is tuple:
                aggr = ops[aggr[1]](aggr[0], int(item))
            elif type(aggr) is str:
                aggr += item
            elif aggr is None:
                aggr = item
            else:
                raise Exception('Unexpected character combination', idx)
        elif item == '(':
            stack.append(aggr)
            aggr = None
        elif item == ')':
            stack_itm = stack.pop()
            if stack_itm is not None:
                aggr = ops[stack_itm[1]](stack_itm[0], int(aggr))
        elif item in ops.keys():
            aggr = (int(aggr), item)
        else:
            raise Exception('Invalid character', item)
    return aggr

print('Part 1:', sum([parse(l) for l in lines]))


def find_char(inp, ch):
    return [idx for idx, char in enumerate(inp) if char == ch]

def add_parentheses(inp):
    inp = list(inp)

    plus_ctr = 0
    while plus_ctr < inp.count('+'):
        plus_indices = find_char(inp, '+')
        plus_ctr_index = plus_indices[plus_ctr]
        left, right = plus_ctr_index-1, plus_ctr_index+1

        if inp[left] == ')':
            stack = [')']
            while stack:
                left -= 1
                if inp[left] == ')':
                    stack.append(')')
                elif inp[left] == '(':
                    stack.pop()

        if inp[right] == '(':
            stack = ['(']
            while stack:
                right += 1
                if inp[right] == '(':
                    stack.append('(')
                elif inp[right] == ')':
                    stack.pop()

        inp.insert(right+1, ')')
        inp.insert(left, '(')

        plus_ctr += 1

    return ''.join(inp)

print('Part 2:', sum([eval(add_parentheses(l)) for l in lines]))
