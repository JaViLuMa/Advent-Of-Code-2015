weapons = [
    {'cost': 8, 'damage': 4, 'armor': 0, 'name': 'Dagger'},
    {'cost': 10, 'damage': 5, 'armor': 0, 'name': 'Shortsword'},
    {'cost': 25, 'damage': 6, 'armor': 0, 'name': 'Warhammer'},
    {'cost': 40, 'damage': 7, 'armor': 0, 'name': 'Longsword'},
    {'cost': 74, 'damage': 8, 'armor': 0, 'name': 'Greataxe'},
]

armor = [
    {'cost': 0, 'damage': 0, 'armor': 0, 'name': 'Nothing'},
    {'cost': 13, 'damage': 0, 'armor': 1, 'name': 'Leather'},
    {'cost': 31, 'damage': 0, 'armor': 2, 'name': 'Chainmail'},
    {'cost': 53, 'damage': 0, 'armor': 3, 'name': 'Splintnmail'},
    {'cost': 75, 'damage': 0, 'armor': 4, 'name': 'Bandedmail'},
    {'cost': 102, 'damage': 0, 'armor': 5, 'name': 'Platemail'},
]

rings = [
    {'cost': 0, 'damage': 0, 'armor': 0, 'name': 'Damage +0'},
    {'cost': 25, 'damage': 1, 'armor': 0, 'name': 'Damage +1'},
    {'cost': 25, 'damage': 1, 'armor': 0, 'name': 'Damage +1'},
    {'cost': 50, 'damage': 2, 'armor': 0, 'name': 'Damage +2'},
    {'cost': 100, 'damage': 3, 'armor': 0, 'name': 'Damage +3'},
    {'cost': 0, 'damage': 0, 'armor': 0, 'name': 'Defense +0'},
    {'cost': 20, 'damage': 0, 'armor': 1, 'name': 'Defense +1'},
    {'cost': 40, 'damage': 0, 'armor': 2, 'name': 'Defense +2'},
    {'cost': 80, 'damage': 0, 'armor': 3, 'name': 'Defense +3'},
]


def simulate(player):
    boss = {'hp': 100, 'armor': 2, 'damage': 8}

    while boss['hp'] > 0 and player['hp'] > 0:
        playerDamage = max(player['damage'] - boss['armor'], 1)
        bossDamage = max(boss['damage'] - player['armor'], 1)

        if player['hp'] > 0:
            boss['hp'] = boss['hp'] - playerDamage

        if boss['hp'] > 0:
            player['hp'] = player['hp'] - bossDamage

    return player['hp'] > 0


minCost = float('inf')
maxCost = 0

for weapon in weapons:
    for mail in armor:
        for ring1 in rings:
            otherRings = [ring for ring in rings if ring['name'] != ring1['name']]

            for ring2 in otherRings:
                player = {
                    'hp': 100,
                    'equipment': [weapon, mail, ring1, ring2],
                    'cost': weapon['cost'] + mail['cost'] + ring1['cost'] + ring2['cost'],
                    'armor': weapon['armor'] + mail['armor'] + ring1['armor'] + ring2['armor'],
                    'damage': weapon['damage'] + mail['damage'] + ring1['damage'] + ring2['damage'],
                }

                if simulate(player):
                    minCost = min(player['cost'], minCost)

                else:
                    maxCost = max(player['cost'], maxCost)

print(f'Part 1: {minCost} | Part 2: {maxCost}')
