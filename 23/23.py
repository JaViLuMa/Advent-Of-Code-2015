def run(instructions, registers):
    i = 0

    while i < len(instructions):
        instruction = instructions[i]

        if instruction.startswith('hlf'):
            registers[instruction[4]] /= 2

            i += 1

        elif instruction.startswith('tpl'):
            registers[instruction[4]] *= 3
            
            i += 1
        
        elif instruction.startswith('inc'):
            registers[instruction[4]] += 1
            
            i += 1
        
        elif instruction.startswith('jmp'):
            i += int(instruction[4:])
        
        elif instruction.startswith('jie'):
            if registers[instruction[4]] % 2 == 0:
                i += int(instruction[7:])
            
            else:
                i += 1
        
        elif instruction.startswith('jio'):
            if registers[instruction[4]] == 1:
                i += int(instruction[7:])
            
            else:
                i += 1
    
    return registers['b']


with open('data.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

registers = {'a': 0, 'b': 0}

registerB = run(instructions, registers)

registers = {'a': 1, 'b': 0}

registerB2 = run(instructions, registers)

print(f'Part 1: {registerB} | Part 2: {registerB2}')
