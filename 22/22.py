from collections import namedtuple

Spell = namedtuple('Spell', ['mana_cost', 'damage', 'heal', 'armour', 'mana_gain', 'duration', 'index'])

missile = Spell(53, 4, 0, 0, 0, 0, 0)
drain = Spell(73, 2, 2, 0, 0, 0, 1)
shield = Spell(113, 0, 0, 7, 0, 6, 2)
poison = Spell(173, 3, 0, 0, 0, 6, 3)
recharge = Spell(229, 0, 0, 0, 101, 5, 4)

spells = [missile, drain, shield, poison, recharge]

leastManaUsed = float('inf')


def fight(bossHp, pHp, pMana, activeSpells, pTurn, manaUsed, hardMode):
    bossDmg = 8
    pArmor = 0

    if hardMode and pTurn:
        pHp -= 1

        if pHp <= 0:
            return False

    _activeSpells = []

    for activeSpell in activeSpells:
        if activeSpell.duration >= 0:             
            bossHp -= activeSpell.damage
            pHp += activeSpell.heal
            pArmor += activeSpell.armour
            pMana += activeSpell.mana_gain

        _activeSpell = Spell(
            activeSpell.mana_cost,
            activeSpell.damage,
            activeSpell.heal,
            activeSpell.armour,
            activeSpell.mana_gain,
            activeSpell.duration - 1,
            activeSpell.index
        )

        if _activeSpell.duration > 0:
            _activeSpells.append(_activeSpell)

    if bossHp <= 0:
        global leastManaUsed

        if manaUsed < leastManaUsed:
            leastManaUsed = manaUsed

        return True

    if manaUsed >= leastManaUsed:
        return False

    if pTurn:
        for spell in spells:
            spell_already_active = any(
                spell.index == active_spell.index for active_spell in _activeSpells
            )

            if spell.mana_cost <= pMana and not spell_already_active:
                newActiveSpells = list(_activeSpells)
                newActiveSpells.append(spell)

                fight(bossHp, pHp, pMana - spell.mana_cost, newActiveSpells, False, manaUsed + spell.mana_cost, hardMode)
    else:
        pHp += pArmor - bossDmg if pArmor - bossDmg < 0 else -1

        if pHp > 0:
            fight(bossHp, pHp, pMana, _activeSpells, True, manaUsed, hardMode)


def preparations(hardMode=False):
    if hardMode:
        global leastManaUsed

        leastManaUsed = float('inf')

    bossHp = 55
    
    playerHp = 50
    playerMana = 500

    playerTurn = True

    fight(bossHp, playerHp, playerMana, [], playerTurn, 0, hardMode)
    
    return leastManaUsed


print(f'Part 1: {preparations()} | Part 2: {preparations(True)}')
