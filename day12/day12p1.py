with open('input.txt') as file:
    data_input = file.read().split()

def main():
    direction = 'E'
    y = 0
    x = 0
    for instruction in data_input:
        if instruction[0] == 'N':
            y += int(instruction[1:])
        elif instruction[0] == 'S':
            y -= int(instruction[1:])
        elif instruction[0] == 'E':
            x += int(instruction[1:])
        elif instruction[0] == 'W':
            x -= int(instruction[1:])
        elif instruction[0] == 'F':
            if direction == 'N':
                y += int(instruction[1:])
            elif direction == 'S':
                y -= int(instruction[1:])
            elif direction == 'E':
                x += int(instruction[1:])
            elif direction == 'W':
                x -= int(instruction[1:])
        elif instruction[0] == 'R' or 'L':
            direction = dir_change(direction, instruction[0], int(instruction[1:]))
    return abs(x) + abs(y)

def dir_change(dir, turn, degrees):
    if dir == 'N':
        if turn == 'L' and degrees == 90:
            return 'W'
        elif turn == 'L' and degrees == 180:
            return 'S'
        elif turn == 'L' and degrees == 270:
            return 'E'
        elif turn == 'R' and degrees == 90:
            return 'E'
        elif turn == 'R' and degrees == 180:
            return 'S'
        elif turn == 'R' and degrees == 270:
            return 'W'
    elif dir == 'S':
        if turn == 'L' and degrees == 90:
            return 'E'
        elif turn == 'L' and degrees == 180:
            return 'N'
        elif turn == 'L' and degrees == 270:
            return 'W'
        elif turn == 'R' and degrees == 90:
            return 'W'
        elif turn == 'R' and degrees == 180:
            return 'N'
        elif turn == 'R' and degrees == 270:
            return 'E'
    elif dir == 'E':
        if turn == 'L' and degrees == 90:
            return 'N'
        elif turn == 'L' and degrees == 180:
            return 'W'
        elif turn == 'L' and degrees == 270:
            return 'S'
        elif turn == 'R' and degrees == 90:
            return 'S'
        elif turn == 'R' and degrees == 180:
            return 'W'
        elif turn == 'R' and degrees == 270:
            return 'N'
    elif dir == 'W':
        if turn == 'L' and degrees == 90:
            return 'S'
        elif turn == 'L' and degrees == 180:
            return 'E'
        elif turn == 'L' and degrees == 270:
            return 'N'
        elif turn == 'R' and degrees == 90:
            return 'N'
        elif turn == 'R' and degrees == 180:
            return 'E'
        elif turn == 'R' and degrees == 270:
            return 'S'
    return None


print('The solution to part 1 is : {}'.format(main()))


