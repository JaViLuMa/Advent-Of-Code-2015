import ast

codeLength = 0
memoryLength = 0
encodeLength = 0

with open('data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        
        codeLength += len(line)

        memoryLength += len(ast.literal_eval(line))

        encodeLength += 2 + line.count('\\') + line.count('"')

print(f'Part 1: {codeLength - memoryLength} | Part 2: {encodeLength}')
