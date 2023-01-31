target = 33100000


def targetHouse(limit=False):
    presents = [0] * (target // (10 if not limit else 11) + 1)
    visitedHouses = [0] * (target // 11 + 1)

    for elf in range(1, len(presents)):
        for house in range(elf, len(presents), elf):
            if not limit:
                presents[house] += elf * 10
            else:
                visitedHouses[elf] += 1

                if visitedHouses[elf] <= 50:
                    presents[house] += elf * 11

    for house in range(1, len(presents)):
        if presents[house] >= target:
            return house


print(f'Part 1: {targetHouse()} | Part 2: {targetHouse(True)}')
