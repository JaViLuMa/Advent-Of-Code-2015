import re

replacements = {}
reversedReplacements = {}


def replaceMe(m):
    return reversedReplacements[m.group()]


with open('data.txt') as f:
    lines = f.read().splitlines()
    
    while line:= lines.pop(0):
        match = re.match(r'(\w+) => (\w+)', line)

        if match:
            toReplace, withString = match.groups()

            if toReplace not in replacements:
                replacements[toReplace] = []

            replacements[toReplace].append(withString)

            reversedReplacements[withString[::-1]] = toReplace[::-1]
        
    molecule = lines[-1]

molecules = set()

for toReplace, withs in replacements.items():
    for with_ in withs:
        for match in re.finditer(toReplace, molecule):
            start, end = match.span()

            newMolecule = molecule[:start] + with_ + molecule[end:]

            molecules.add(newMolecule)

distinctMolecules = len(molecules)

steps = 0

molecule = molecule[::-1]

while molecule != 'e':
    molecule = re.sub('|'.join(reversedReplacements.keys()), replaceMe, molecule, 1)

    steps += 1

print(f'Part 1: {distinctMolecules} | Part 2: {steps}')
