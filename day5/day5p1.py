"""Solution for day 5, part 1 puzzle on adventofcode.com"""

with open(file='input.txt',mode='rt',encoding='utf-8',newline='\n') as file:
    seat_manifest = []
    for line in file.readlines():
        seat_manifest.append(line.strip('\n'))


def find_row(input):
    f_row = 0
    b_row = 128
    for char in input.strip('LR'):
        if char == 'F':
            b_row = b_row - ((b_row - f_row) / 2)
        elif char == 'B':
            f_row = f_row + ((b_row - f_row) / 2)
    return int(f_row)


def find_column(input):
    l_col = 0
    r_col = 8
    for char in input.strip('FB'):
        if char == 'L':
            r_col = r_col - ((r_col - l_col) /2)
        elif char == 'R':
            l_col = l_col + ((r_col - l_col) /2)
    return int(l_col)


def find_seat_num():
    list_seat_numbers = []
    for line in seat_manifest:
        seat_row = find_row(line)
        seat_col = find_column(line)
        seat_num = (seat_row * 8) + seat_col
        list_seat_numbers.append(seat_num)
    list_seat_numbers.sort()
    return list_seat_numbers


print(find_seat_num()[-1])




