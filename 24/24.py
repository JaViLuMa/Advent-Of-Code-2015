from functools import reduce
from itertools import combinations


def smallestQuantumEntanglement(parts, presentWeights):
    groupWeight = sum(presentWeights) // parts

    for i in range(len(presentWeights)):
        quantumEntanglements = [reduce(lambda x, y: x * y, c) for c in combinations(presentWeights, i) if sum(c) == groupWeight]

        if quantumEntanglements:
            return min(quantumEntanglements)


with open('data.txt') as f:
    presentWeights = [int(line) for line in f.readlines()]

print(f'Part 1: {smallestQuantumEntanglement(3, presentWeights)} | Part 2: {smallestQuantumEntanglement(4, presentWeights)}')
