"""Solution for day 6, part 1 puzzle on adventofcode.com"""

with open(file='input.txt',mode='rt',encoding='utf-8') as file:
    l = file.read().split('\n\n')
    customs_list = []
    for item in l:
        customs_list.append(item.replace('\n',''))
    complete_set = []
    for item in customs_list:
        response_set = set()
        for response in item:
            response_set.add(response)
        complete_set.append(response_set)

def calculate_responses(input):
    total = 0
    for i in input:
        total += len(i)
    return total

print(calculate_responses(complete_set))