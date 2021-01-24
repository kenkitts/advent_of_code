from time import time

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

def scan_error_rate():
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

scan_error_rate()

stop_time = time()
total_time = stop_time - start_time

print('The solution to day 16, part 1 is {}\n'
      'It took {} seconds to execute.'.format(sum(bad_values),total_time))

