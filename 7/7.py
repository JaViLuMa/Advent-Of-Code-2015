wires = {}
cache = {}


def solveCircuit(node):
    if node.isnumeric():
        return int(node)
    
    if node not in cache:
        instructions = wires[node]

        if len(instructions) == 1:
            cache[node] = solveCircuit(instructions[0])

        else:
            instruction = instructions[-2]

            if instruction == 'AND':
                cache[node] = solveCircuit(instructions[0]) & solveCircuit(instructions[2])

            elif instruction == 'OR':
                cache[node] = solveCircuit(instructions[0]) | solveCircuit(instructions[2])

            elif instruction == 'LSHIFT':
                cache[node] = solveCircuit(instructions[0]) << solveCircuit(instructions[2])

            elif instruction == 'RSHIFT':
                cache[node] = solveCircuit(instructions[0]) >> solveCircuit(instructions[2])

            elif instruction == 'NOT':
                cache[node] = ~solveCircuit(instructions[1])

    return cache[node]


with open('data.txt') as f:
    for line in f:
        wire = line.rstrip().split(' -> ')

        wires[wire[-1]] = wire[0].split()

wireA = solveCircuit('a')
wires['b'] = [str(wireA)]

cache = {}

print(f'Part 1: {wireA} | Part 2: {solveCircuit("a")}')
