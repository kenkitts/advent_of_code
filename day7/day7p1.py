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

"""Define a function that searches through the bag_data for bags
 that contain the target.  If they do, then the function will
 call itself (recursion)"""

def find_bag(bag_data, target):
    global bag_set
    for bag in bag_data:
        if target in bag_data[bag].keys():
            bag_set.add(bag)
            find_bag(bag_data, bag)

find_bag(bag_data, target)

print('The solution to part 1 is: {p1}'.format(p1=len(bag_set)))