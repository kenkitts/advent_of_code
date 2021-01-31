from time import time
from pprint import pprint as pp

###Start time
start_time = time()

###Create data structures
fields = list()
tickets = list()
mmap = dict()
bad_values = list()


###Open input file and massage data into data structures
with open('input.txt','rt') as file:
    for i in file.readlines():
        if i[0].isalpha() and 'ticket' not in i:
            line = list()
            line.append(i.split(':')[0])
            line.append(range(int(i.split(': ')[1].split(' ')[0].split('-')[0]),
                        int(i.split(': ')[1].split(' ')[0].split('-')[1]) + 1))
            line.append(range(int(i.split(': ')[1].split(' ')[2].strip('\n').split('-')[0]),
                        int(i.split(': ')[1].split(' ')[2].strip('\n').split('-')[1]) + 1))
            line.append(list())
            fields.append(line)
        elif i[0].isnumeric():
            line = list()
            for n in i.split(','):
                line.append(int(n.strip('\n')))
            tickets.append(line)


def check_validity(number,range_1,range_2):
    if number in range_1 or number in range_2:
        return True
    else:
        return False


def p1():
    for line in tickets:
        for number in line:
            if number in mmap.keys():
                if mmap[number] is True:
                    continue
                elif mmap[number] is False:
                    bad_values.append(number)
                    continue
            for field in fields:
                if check_validity(number,field[1],field[2]) is True:
                    mmap[number] = True
                    break
                else:
                    mmap[number] = False
            if mmap[number] is False:
                bad_values.append(number)


def p2():
    valid_tickets = list()
    for line in tickets:
        for number in line:
            if mmap[number] is False:
                break
        else:
            valid_tickets.append(line)

    for i_field in fields:
        position = 0
        while position < len(valid_tickets[0]):
            for i_ticket in valid_tickets:
                if i_ticket[position] in i_field[1] or \
                    i_ticket[position] in i_field[2]:
                    continue
                else:
                    position += 1
                    break
            else:
                i_field[3].append(position)
                position += 1



p1()

stop_time_p1 = time()
total_time_p1 = stop_time_p1 - start_time

print('The solution to day 16, part 1 is {}\n'
      'It took {} seconds to execute.'.format(sum(bad_values),total_time_p1))

p2()

fields.sort(key = lambda x: len(x[3]))

removals = list()
for x,y in enumerate(fields):
    if len(removals) > 0:
        for i in removals:
            fields[x][3].remove(i)
    removals.append(y[3][0])

answer = 1
for i in fields:
    if i[0].startswith('departure'):
        answer = answer * tickets[0][i[3][0]]

stop_time_p2 = time()
total_time_p2 = stop_time_p2 - stop_time_p1

print('The solution to day 16, part 2 is {}\n'
      'It took {} seconds to execute.'.format(answer,total_time_p2))