with open('input.txt','rt') as file:
    data = file.read().split(',')

turn = len(data) + 1

while turn <= 2020:
    if data.count(data[-1]) > 1:
        reversed_data = data[-2::-1]
        idx = reversed_data.index(data[-1])
        last_num_spoken = idx + 1
        data.append(str(last_num_spoken))
    else:
        data.append('0')
    turn +=1

print(data[-1])