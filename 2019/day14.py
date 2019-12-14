from collections import defaultdict
from math import ceil

product_requirements, reaction_amounts = {}, {}
for l in open('input14').readlines():
    reaction = [r.split(',') for r in l.strip().split('=>')]
    inputs, output = reaction[0], reaction[1][0]
    inputs = [i.strip().split(' ') for i in inputs]
    output = output.strip().split(' ')
    product_requirements[output[1]] = [(int(a), b) for [a, b] in inputs]
    reaction_amounts[output[1]] = int(output[0])

def mine(element, quantity):
    if element == 'ORE':
        used[element] += quantity
    else:
        if quantity <= excess[element]:
            used[element] += quantity
            excess[element] -= quantity
        else:
            quantity = quantity - excess[element]
            used[element] += excess[element]
            excess[element] = 0

            reactions_needed = int(ceil(float(quantity) / reaction_amounts[element]))
            for (q, elem) in product_requirements[element]:
                mine(elem, reactions_needed * q)

            used[element] += quantity
            excess[element] += reactions_needed * reaction_amounts[element] - quantity

used, excess = defaultdict(int), defaultdict(int)
mine('FUEL', 1)
print 'Part 1:', used['ORE']

max_ore = 1000000000000
fuels_min, fuels_max = max_ore / used['ORE'], max_ore
while fuels_min < fuels_max:
    mid_fuel = (fuels_max + fuels_min) / 2
    used, excess = defaultdict(int), defaultdict(int)
    mine('FUEL', mid_fuel)
    if used['ORE'] > max_ore:
        fuels_max = mid_fuel - 1
    elif used['ORE'] < max_ore:
        fuels_min = mid_fuel + 1
    else:
        fuels_max = mid_fuel
        break
print 'Part 2:', fuels_max
