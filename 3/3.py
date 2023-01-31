def updateDirValuesAndVisitedHouses(x, y, houses):
    if dir == '^':
        y += 1
    elif dir == 'v':
        y -= 1
    elif dir == '<':
        x -= 1
    elif dir == '>':
        x += 1

    houses.add((x, y))

    return [x, y]


with open('data.txt', 'r') as f:
    directions = f.read()

    bothX, bothY, santaX, santaY, roboX, roboY = 0, 0, 0, 0, 0, 0

    housesBoth = set()
    housesSanta = set()
    housesRobo = set()

    housesBoth.add((bothX, bothY))
    housesSanta.add((santaX, santaY))
    housesRobo.add((roboX, roboY))

    for index, dir in enumerate(directions):
        bothX, bothY = updateDirValuesAndVisitedHouses(bothX, bothY, housesBoth)

        if index % 2 == 0:
            santaX, santaY = updateDirValuesAndVisitedHouses(santaX, santaY, housesSanta)
        else:
            roboX, roboY = updateDirValuesAndVisitedHouses(roboX, roboY, housesRobo)


print(f'Part 1: {len(housesBoth)} | Part 2: {len(housesSanta.union(housesRobo))}')
