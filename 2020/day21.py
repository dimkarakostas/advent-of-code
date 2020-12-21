lines = [l.strip() for l in open('input21').readlines()]

foods = []
for l in lines:
    splitted = l[:-1].split(' (contains ')
    ingredients, allergens = splitted[0].split(), splitted[1].split(', ')
    foods.append([ingredients, allergens])

ingredients = set().union(*[f[0] for f in foods])
allergens = set().union(*[f[1] for f in foods])

appearances = {ing: 0 for ing in ingredients}
candidates = {al: ingredients for al in allergens}
for (food_ingredients, food_allergens) in foods:
    for al in food_allergens:
        candidates[al] = candidates[al].intersection(food_ingredients)
    for ing in food_ingredients:
        appearances[ing] += 1

found = {}
while len(candidates.keys()) > 0:
    for al in candidates.keys():
        if len(candidates[al]) == 1:
            found[al] = next(iter(candidates[al]))
    for al in set(found.keys()).intersection(set(candidates.keys())):
        del candidates[al]
    for al in candidates.keys():
        candidates[al] -= set(found.values())

print('Part 1:', sum([appearances[i] for i in ingredients - set(found.values())]))
print('Part 2:', ','.join([i[1] for i in sorted(found.items())]))
