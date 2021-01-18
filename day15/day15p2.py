import time

start_time = time.time()

target_turn = 30000000

with open('input.txt','rt') as file:
    data = (int(i) for i in file.read().split(','))
    data_map = {**dict.fromkeys(range(0,target_turn + 1),None)}
    for value,key in enumerate(data):
        data_map[key] = value + 1


def main():
    turn = value + 2
    next_number = 0
    old_turn = None
    while turn <= target_turn:
        if next_number in data_map.keys() and old_turn is not None:
            next_number = data_map[next_number] - old_turn
            if data_map[next_number] is not None:
                old_turn = data_map[next_number]
            else:
                old_turn = None
            data_map[next_number] = turn
        else:
            next_number = 0
            if data_map[next_number] is not None:
                old_turn = data_map[0]
            data_map[next_number] = turn
        turn +=1
    return next_number

print('The solution is: {}'.format(main()))

stop_time = time.time()
print('Code took {} seconds to complete.'.format(stop_time - start_time))


