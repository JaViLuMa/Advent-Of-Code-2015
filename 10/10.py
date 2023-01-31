def lookAndSay(s):
    result = ''

    i = 0

    while i < len(s):
        count = 1

        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1

            count += 1
        
        result += str(count) + s[i]
        
        i += 1

    return result


def repeatSay(n):
    sayMe = '1113222113'

    for _ in range(n):
        sayMe = lookAndSay(sayMe)

    return sayMe


print(f'Part 1: {len(repeatSay(40))} | Part 2: {len(repeatSay(50))}')
