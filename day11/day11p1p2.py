from pprint import pprint as pp

seat_map = [i.strip() for i in open('input.txt', 'rt')]
width = (len(seat_map[0]) - 1)
length = (len(seat_map) - 1)

def adj_check(seat_map,row,col,r_step,c_step):
    try:
        while True:
            row += r_step
            col += c_step
            if row >= 0 and col >= 0:
                if seat_map[row][col] == '#':
                    return '#'
                elif seat_map[row][col] == 'L':
                    return 'L'
            else:
                return None
    except IndexError:
        return None


def seat_check(seat_map,row,col):
    current_seat = seat_map[row][col]
    adj_seats = list()
    adj_seats.append(adj_check(seat_map,row,col,-1,-1) \
                         if row > 0 and col > 0 else None)
    adj_seats.append(adj_check(seat_map,row,col,-1,0) \
                         if row > 0 else None)
    adj_seats.append(adj_check(seat_map,row,col,-1,1) \
                         if row > 0 and col < width else None)
    adj_seats.append(adj_check(seat_map,row,col,0,-1) \
                         if col > 0 else None)
    adj_seats.append(adj_check(seat_map,row,col,0,1) \
                         if col < width else None)
    adj_seats.append(adj_check(seat_map,row,col,1,-1) \
                         if row < length and col > 0 else None)
    adj_seats.append(adj_check(seat_map,row,col,1,0) \
                         if row < length else None)
    adj_seats.append(adj_check(seat_map,row,col,1,1) \
                         if row < length and col < width else None)
    if current_seat == 'L':
        if adj_seats.count('#') > 0:
            return 'L'
        else:
            return '#'
    elif current_seat == '#':
        if adj_seats.count('#') >= 5:
            return 'L'
        else:
            return '#'

def main(seat_map):
    revised_seat_map= []
    for c_row,row in enumerate(seat_map):
        revised_row = ''
        for c_col,col in enumerate(row):
            if col == '.':
                revised_row += '.'
                continue
            revised_row += (seat_check(seat_map,c_row,c_col))
        revised_seat_map.append(revised_row)
    return revised_seat_map


while seat_map != main(seat_map):
    seat_map = main(seat_map)

seat_count = sum(seat_map[c].count('#') for c,i in enumerate(seat_map))

pp('The total number of seats occupied for part 2 is: {}'.format(seat_count))

