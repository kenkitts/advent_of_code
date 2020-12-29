with open('input.txt','rt') as file:
    instructions = file.read().split('\n')


def start(instructions, x):
    global total, history
    while x not in history:
        if x >= len(instructions):
            print('The solution to part 2 is: {}'.format(total))
            return total
        history.append(x)
        if instructions[x].split()[0] == 'acc':
            total += int(instructions[x].split()[1])
            start(instructions, x + 1)
        elif instructions[x].split()[0] == 'jmp':
            start(instructions, x + int(instructions[x].split()[1]))
        elif instructions[x].split()[0] == 'nop':
            start(instructions, x + 1)
    return total

history = []
total = 0
print('The solution to part 1 is: {}'.format(start(instructions, 0)))

l_num = 0
for line in instructions:
    history = []
    total = 0
    instructions_alt = instructions.copy()
    if line.startswith('nop'):
        line = line.replace('nop','jmp')
    elif line.startswith('jmp'):
        line = line.replace('jmp','nop')
    else:
        l_num += 1
        continue
    instructions_alt[l_num] = line
    start(instructions_alt,0)
    l_num += 1


