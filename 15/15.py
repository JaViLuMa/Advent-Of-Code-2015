import re
from itertools import permutations


def getHighestScore(ingredients, perms, containsCalories=False):
    maxScore = 0

    for perm in perms:
        capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0

        for index, ingredient in enumerate(ingredients):
            capacity += ingredients[ingredient]['capacity'] * perm[index]
            durability += ingredients[ingredient]['durability'] * perm[index]
            flavor += ingredients[ingredient]['flavor'] * perm[index]
            texture += ingredients[ingredient]['texture'] * perm[index]
            calories += ingredients[ingredient]['calories'] * perm[index]

        if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
            continue

        if containsCalories and calories != 500:
            continue

        score = capacity * durability * flavor * texture

        maxScore = max(score, maxScore)

    return maxScore


ingredients = {}

with open('data.txt') as f:
    for line in f:
        matches = re.match(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)

        if matches:
            ingredient, capacity, durability, flavor, texture, calories = matches.groups()

            ingredients[ingredient] = {
                'capacity': int(capacity),
                'durability': int(durability),
                'flavor': int(flavor),
                'texture': int(texture),
                'calories': int(calories)
            }


numbers = list(range(0, 101))

perms = permutations(numbers, 4)

filteredPerms = list(filter(lambda x: sum(x) == 100, perms))

print(f'Part 1: {getHighestScore(ingredients, filteredPerms)} | Part 2: {getHighestScore(ingredients, filteredPerms, True)}')
