"""Solution for day 6, part 2 puzzle on adventofcode.com"""

with open(file='input.txt',mode='rt',encoding='utf-8') as file:
    l = file.read().split('\n\n')
    customs_list = list()
    for i in l:
        temp_list = i.split('\n')
        customs_list.append(temp_list)


def calc_responses(list_data):
    group_size = len(list_data)
    count = 0
    string = ''
    if group_size == 1:
        return len(list_data[0])
    for x in list_data:
        string += x
    for x in set(string):
        if string.count(x) == group_size:
            count +=1
    return count

def main():
    total_count = 0
    for y in customs_list:
        total_count += calc_responses(y)
    return total_count

print('The total number of yes responses is {}.'.format(main()))

