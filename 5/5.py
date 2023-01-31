import re

niceStringsPart1 = 0
niceStringsPart2 = 0

with open('data.txt') as f:
    strings = f.read().splitlines()

for string in strings:
    vowels = re.findall(r'[aeiou]', string)

    if len(vowels) < 3:
        continue

    if not re.search(r'(\w)\1', string):
        continue

    if re.search(r'ab|cd|pq|xy', string):
        continue

    niceStringsPart1 += 1


for string in strings:
    if not re.search(r'(..).*\1', string):
        continue

    if not re.search(r'(.).\1', string):
        continue

    niceStringsPart2 += 1

print(f'Part 1: {niceStringsPart1} | Part 2: {niceStringsPart2}')
