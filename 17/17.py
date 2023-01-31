from itertools import combinations

containers = [int(line.strip()) for line in open('data.txt')]

numOfCombinations = 0
containerCombinations = []

for length in range(1, len(containers) + 1):
    for combo in combinations(containers, length):
        if sum(combo) == 150:
            numOfCombinations += 1
            containerCombinations.append(combo)

minContainers = min([len(combo) for combo in containerCombinations])

numOfMinCombinations = 0

for combo in containerCombinations:
    if len(combo) == minContainers:
        numOfMinCombinations += 1

print(f'Part 1: {numOfCombinations} | Part 2: {numOfMinCombinations}')
