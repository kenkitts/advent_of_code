import time

start_time = time.time()

with open('input.txt','rt') as file:
    data = file.read().split(',')
    data_map = {}
    for value,key in enumerate(data):
        data_map[key] = value + 1


def main():
    turn = len(data) + 1
    next_number = ''
    old_turn = None
    while turn <= 30000000:
        if next_number in data_map.keys() and old_turn is not None:
            next_number = str(data_map[next_number] - old_turn)
            if str(next_number) in data_map.keys():
                old_turn = data_map[next_number]
            else:
                old_turn = None
            data_map[next_number] = turn
        else:
            next_number = '0'
            if str(next_number) in data_map.keys():
                old_turn = data_map['0']
            data_map[next_number] = turn
        turn +=1
    return next_number

print(main())

stop_time = time.time()
print('Code took {} seconds to complete.'.format(stop_time - start_time))


