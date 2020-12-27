"""Open input file and format data into a dictionary object called bag_data."""

with open('input.txt','rt') as file:
    l = (file.read().replace('bags contain','|')
                .replace('bags','')
                .replace('bag','')
                .replace('.','')
                .replace(',','|')
                .split('\n'))
    bag_list = []
    for line in l:
        bag_list.append(line.split('|'))
    bag_data = {}
    for line in bag_list:
        temp_dict = {}
        bag_name = line[0].rstrip(' ')
        line.pop(0)
        for bag in line:
            bag = bag.lstrip(' ').rstrip(' ')
            if bag.isalpha():
                value = int(1)
            elif bag == 'no other':
                break
            else:
                value = int(bag[0])
                bag = bag.lstrip(str(value)).lstrip(' ')
            key = bag
            temp_dict.update({key:value})
        bag_data.update({bag_name:temp_dict})


target = 'shiny gold'
bag_set = set()


def p1(bag_data, target):
    global bag_set
    for bag in bag_data:
        if target in bag_data[bag].keys():
            bag_set.add(bag)
            p1(bag_data, bag)
    return len(bag_set)


def p2(bag_data, target):
    count = 0
    if bool(bag_data.get(target)):
        for key in bag_data.get(target):
            bag_count = bag_data[target][key]
            count += bag_count + (bag_count * (p2(bag_data, key)))
    return count


print('The solution to part 1 is: {}'.format(p1(bag_data, target)))
print('The solution to part 2 is: {}'.format(p2(bag_data, target)))