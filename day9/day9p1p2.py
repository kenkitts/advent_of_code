#!/usr/bin/env python3

data = [int(line.strip('\n')) for line in open(file='input.txt',mode='rt')]

def p1(i_list, i):
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
        if p1(i_list, i) is False:
            return i
        else:
            start_index += 1
            end_index += 1


def p2(data, target):
    for l_idx,v in enumerate(data):
        num_list = [v]
        total = v
        r_idx = l_idx + 1
        while total < target:
            total += data[r_idx]
            num_list.append(data[r_idx])
            if total == target:
                return sorted(num_list)[0] + sorted(num_list)[-1]
            r_idx += 1


if __name__ == '__main__':
    print('The solution to part 1 is : {}'.format(main(data, 25)))
    print('The solution to part 2 is : {}'.format(p2(data, main(data, 25))))