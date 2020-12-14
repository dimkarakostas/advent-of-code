import re

lines = [l.strip() for l in open('input14').readlines()]

rg = r'^mem\[(\w+)\] = (\w+)$'
programs = []
for l in lines:
    if 'mask' in l:
        mask = l.split(' = ')[1]
        programs.append([mask])
        continue
    m = re.match(rg, l)
    mem_position, val = m.groups()
    programs[-1].append((mem_position, val))


memory = {}
for p in programs:
    mask = p[0]
    for mem_position, val in p[1:]:
        memory[mem_position] = ''
        val = '{0:b}'.format(int(val))
        val = '0'*(len(mask) - len(val)) + val
        for bit_idx in range(len(val)):
            memory[mem_position] += mask[bit_idx] if mask[bit_idx] != 'X' else val[bit_idx]
print('Part 1:', sum([int(v, 2) for v in memory.values()]))


memory = {}
for p in programs:
    mask = p[0]
    for mem_position, val in p[1:]:
        mem_position = '{0:b}'.format(int(mem_position))
        mem_position_list = list('0'*(len(mask) - len(mem_position)) + mem_position)
        for bit_idx in range(len(mask)):
            if mask[bit_idx] != '0':
                mem_position_list[bit_idx] = mask[bit_idx]
        mem_position = ''.join(mem_position_list)
        mem_list = []
        if mem_position[0] != 'X':
            mem_list = [mem_position[0]]
        else:
            mem_list = ['0', '1']

        for bit_idx in range(1, len(mem_position)):
            if mem_position[bit_idx] != 'X':
                for idx in range(len(mem_list)):
                    mem_list[idx] += mem_position[bit_idx]
            else:
                new_list = []
                for idx, item in enumerate(mem_list):
                    new_list.append(item + '0')
                    mem_list[idx] += '1'
                mem_list += new_list
        for mem in mem_list:
            memory[mem] = int(val)
print('Part 2:', sum([v for v in memory.values()]))
