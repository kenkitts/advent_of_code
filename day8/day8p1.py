with open('input.txt','rt') as file:
    instructions = file.read().split('\n')

history = []
total = 0

def start(instructions, x):
    global history, total
    while x not in history:
        history.append(x)
        if instructions[x].split()[0] == 'acc':
            total += int(instructions[x].split()[1])
            start(instructions, x + 1)
        elif instructions[x].split()[0] == 'jmp':
            start(instructions, x + int(instructions[x].split()[1]))
        elif instructions[x].split()[0] == 'nop':
            start(instructions, x + 1)
    return total

print('The solution to part 1 is: {}'.format(start(instructions, 0)))

