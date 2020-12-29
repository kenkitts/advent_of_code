data = [int(line.strip('\n')) for line in open(file='input.txt',mode='rt')]

def check(i_list, i):
    index = 0
    result = False
    for num_1 in i_list:
        i_list.pop(index)
        for num_2 in i_list:
            if num_1 + num_2 == i:
                result = True
        i_list.insert(index, num_1)
        index += 1
    return result

def main(data, preamble):
    start_index = 0
    end_index = 25
    while end_index < (len(data)):
        i = data[end_index]
        i_list = data[start_index:end_index]
        if check(i_list,i) is False:
            return i
        else:
            start_index += 1
            end_index += 1


print(main(data,25))