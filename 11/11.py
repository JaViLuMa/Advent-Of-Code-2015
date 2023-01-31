def incrementPassword(s):
    s = list(s)
    i = len(s) - 1

    while i >= 0:
        if s[i] == 'z':
            s[i] = 'a'
            i -= 1
        else:
            s[i] = chr(ord(s[i]) + 1)
            break

    return ''.join(s)


def hasTwoNonOverlappingPairs(s):
    pairs = []
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            pairs.append(s[i])

    return len(set(pairs)) >= 2


def doesNotHaveIOL(s):
    return 'i' not in s and 'o' not in s and 'l' not in s


def hasIncreasingStraight(s):
    for i in range(len(s) - 2):
        if ord(s[i]) == ord(s[i + 1]) - 1 == ord(s[i + 2]) - 2:
            return True

    return False


def isValid(s):
    return (hasIncreasingStraight(s) and
            doesNotHaveIOL(s) and
            hasTwoNonOverlappingPairs(s))


def generatePassword(password):
    while not isValid(password):
        password = incrementPassword(password)

    return password


firstPassword = generatePassword('hepxcrrq')
secondPassword = generatePassword(incrementPassword(firstPassword))

print(f'Part 1: {firstPassword} | Part 2: {secondPassword}')
