lines = [l.strip() for l in open('input13').readlines()]

departure = int(lines[0])
buses = [int(l) for l in lines[1].split(',') if l != 'x']

bus_departures = [b * ((departure//b) + 1) for b in buses]
min_departure = min(bus_departures)
min_bus = buses[bus_departures.index(min_departure)]
print('Part 1:', min_bus * (min_departure - departure))

offsets = {}
for b in buses:
    offsets[b] = lines[1].split(',').index(str(b))

timestamp = buses[0]
aggregate = buses[0]
for b in buses[1:]:
    while (timestamp + offsets[b]) % b != 0:
        timestamp += aggregate
    aggregate *= b
print('Part 2:', timestamp)
