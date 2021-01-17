from copy import deepcopy

with open('input.txt','rt') as file:
    instructions = file.read().split('\n')


def convertp2(num,mask):
    num_bin = list(bin(num).lstrip('0b').zfill(36))
    l = list()
    for idx,char in enumerate(mask):
        if char == '0':
            continue
        elif char == '1':
            num_bin[idx] = '1'
        elif char == 'X':
            num_bin[idx] = 'X'
    l.append(num_bin)
    for idx,char in enumerate(num_bin):
        if char == 'X':
            l_copy = deepcopy(l)
            for i in l_copy:
                i[idx] = '1'
            for i in l:
                i[idx] = '0'
            l.extend(l_copy)
    for x,y in enumerate(l):
        l[x] = int("".join(y),2)
    return l


def main():
    data = {}
    mask = ''
    for i in instructions:
        if 'mask' in i:
            mask = i.lstrip('mask = ')
        elif 'mem' in i:
            start = i.find('[') + 1
            end = i.find(']')
            temp_mask = ""
            for x in range(start, end):
                temp_mask += i[x]
            c_num = convertp2(int(temp_mask),mask)
            for x in c_num:
                data['mem['+str(x)+']'] = int(i.partition('=')[2])
    return data

print(sum(main().values()))

#print('The solution to day 14, part 1 is: {}'.format(sum(main().values())))