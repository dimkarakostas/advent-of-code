lines = [l.strip() for l in open('input4').readlines()]

passports = [[]]
for line in lines:
    passports[-1] += line.split()
    if line == '':
        passports.append([])

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

filled, valid = 0, 0
for pport in passports:
    existing_fields = [False for _ in fields]
    valid_fields = [False for _ in fields]

    for pport_field in pport:
        field_type, field_val = pport_field.split(':')
        try:
            idx = fields.index(field_type)
            existing_fields[idx] = True

            if field_type == 'byr':
                valid_fields[idx] = 1920 <= int(field_val) <= 2002
            elif field_type == 'iyr':
                valid_fields[idx] = 2010 <= int(field_val) <= 2020
            elif field_type == 'eyr':
                valid_fields[idx] = 2020 <= int(field_val) <= 2030
            elif field_type == 'hgt':
                num, unit = int(field_val[:-2]), field_val[-2:]
                valid_fields[idx] = any([
                    unit == 'cm' and 150 <= num <= 193,
                    unit == 'in' and 59 <= num <= 76
                ])
            elif field_type == 'hcl':
                valid_fields[idx] = all([
                    len(field_val) == 7,
                    field_val[0] == '#',
                    int(field_val[1:], 16)
                ])
            elif field_type == 'ecl':
                valid_fields[idx] = field_val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            elif field_type == 'pid':
                valid_fields[idx] = all([
                    len(field_val) == 9,
                    int(field_val)
                ])
        except ValueError:
            pass

    filled += all(existing_fields[:-1])
    valid += all(valid_fields[:-1])

print('Part 1:', filled)
print('Part 2:', valid)
