with open('data.txt') as f:
    instructions = f.read()

    floor = 0
    basementIndex = 0

    for index, i in enumerate(instructions):
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1

        if basementIndex == 0 and floor == -1:
            basementIndex = index + 1

    print(f'Part 1: {floor} | Part 2: {basementIndex}')
