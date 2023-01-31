import re

aunts = {}

correctAuntInfo = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

with open('data.txt') as f:
    for line in f:
        matches = re.match(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)

        if matches:
            aunt, a, aAmount, b, bAmount, c, cAmount = matches.groups()

            aunts[aunt] = {
                a: int(aAmount),
                b: int(bAmount),
                c: int(cAmount)
            }

obviouslyWrongAunt = 0
correctAunt = 0

for aunt, info in aunts.items():
    for key, value in info.items():
        if value != correctAuntInfo[key]:
            break

    else:
        obviouslyWrongAunt = aunt


for aunt, info in aunts.items():
    for key, value in info.items():
        if key in ['cats', 'trees']:
            if value <= correctAuntInfo[key]:
                break

        elif key in ['pomeranians', 'goldfish']:
            if value >= correctAuntInfo[key]:
                break

        elif value != correctAuntInfo[key]:
            break

    else:
        correctAunt = aunt

print(f'Part 1: {obviouslyWrongAunt} | Part 2: {correctAunt}')
