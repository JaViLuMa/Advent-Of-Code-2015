import re
from itertools import permutations


def getMaximumHappiness(happiness, perms):
    maxHappiness = 0

    for perm in perms:
        currHappiness = 0

        for person in range(len(perm) - 1):
            currHappiness += happiness[(perm[person], perm[person + 1])]
            currHappiness += happiness[(perm[person + 1], perm[person])]

        currHappiness += happiness[(perm[-1], perm[0])]
        currHappiness += happiness[(perm[0], perm[-1])]

        maxHappiness = max(maxHappiness, currHappiness)
    
    return maxHappiness


happiness = {}
people = set()

with open('data.txt') as f:
    for line in f:
        matches = re.match(r'(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)', line)
        
        if matches:
            person, gainOrLose, amount, nextTo = matches.groups()

            happiness[(person, nextTo)] = int(amount) * (-1 if gainOrLose == 'lose' else 1)

            people.add(person)

permsOfPeople = permutations(list(people))

withoutMe = getMaximumHappiness(happiness, permsOfPeople)

for person in people:
    happiness[('me', person)] = 0
    happiness[(person, 'me')] = 0

permsOfPeople = permutations(list(people) + ['me'])

withMe = getMaximumHappiness(happiness, permsOfPeople)

print(f'Part 1: {withoutMe} | Part 2: {withMe}')
