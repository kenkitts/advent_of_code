with open('input.txt','rt') as file:
    data = file.readlines()
    time = data[0].strip()
    buses = list()
    for i in data[1].split(','):
        if i.isnumeric():
            buses.append(i)
    buses = sorted(buses)
    del data


def next_departure():
    departures = dict()
    next_bus_time = 9999
    next_bus_num = int()
    for i in buses:
        departures.update({int(i):int(i) - (int(time) % int(i))})
    for key,value in departures.items():
        if value < next_bus_time:
            next_bus_time = value
            next_bus_num = key
    return next_bus_time * next_bus_num

print(next_departure())



print('The current time is {} and the buses running are {}.'.format(time,buses))