with open('input.txt') as file:
    data_input = file.read().split()


def wp_change(x_wp,y_wp,direction,degrees):
    x_wp_new = int()
    y_wp_new = int()
    if direction == "L":
        if degrees == 90:
            x_wp_new = y_wp * -1
            y_wp_new = x_wp
        elif degrees == 180:
            x_wp_new = x_wp * -1
            y_wp_new = y_wp * -1
        elif degrees == 270:
            x_wp_new = y_wp
            y_wp_new = x_wp * -1
    elif direction == "R":
        if degrees == 90:
            x_wp_new = y_wp
            y_wp_new = x_wp * -1
        elif degrees == 180:
            x_wp_new = x_wp * -1
            y_wp_new = y_wp * -1
        elif degrees == 270:
            x_wp_new = y_wp * -1
            y_wp_new = x_wp
    return x_wp_new, y_wp_new


def main():
    x_wp = 10
    y_wp = 1
    x_ferry = 0
    y_ferry = 0
    for instruction in data_input:
        if instruction[0] == 'N':
            y_wp += int(instruction[1:])
        elif instruction[0] == 'S':
            y_wp -= int(instruction[1:])
        elif instruction[0] == 'E':
            x_wp += int(instruction[1:])
        elif instruction[0] == 'W':
            x_wp -= int(instruction[1:])
        elif instruction[0] == 'F':
            x_ferry += int(instruction[1:]) * x_wp
            y_ferry += int(instruction[1:]) * y_wp
        elif instruction[0] == 'R' or 'L':
            x_wp, y_wp = wp_change(x_wp,y_wp,instruction[0],int(instruction[1:]))
    return abs(x_ferry) + abs(y_ferry)


print('The solution to day 12, part 2 is: {}'.format(main()))
