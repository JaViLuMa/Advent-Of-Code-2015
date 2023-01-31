import re
from itertools import permutations

cities = set()
distances = {}

with open('data.txt') as f:
    for line in f:
        match = re.match(r'(\w+) to (\w+) = (\d+)', line)

        if match:
            city1, city2, distance = match.groups()
            distance = int(distance)

            cities.add(city1)
            cities.add(city2)

            distances[(city1, city2)] = distance
            distances[(city2, city1)] = distance

perms = permutations(cities)

routeLengths = []

for perm in perms:
    routeLength = 0

    for i in range(len(perm) - 1):
        routeLength += distances[(perm[i], perm[i + 1])]

    routeLengths.append(routeLength)

print(f'Part 1: {min(routeLengths)} | Part 2: {max(routeLengths)}')
