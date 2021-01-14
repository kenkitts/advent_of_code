with open('input.txt','rt') as file:
    instructions = file.read().split('\n')


def convert(num,mask):
    num_bin = list(bin(num).lstrip('0b').zfill(36))
    for idx,char in enumerate(mask):
        if char == 'X':
            continue
        elif char == '1':
            num_bin[idx] = '1'
        elif char == '0':
            num_bin[idx] = '0'
    num_bin = "".join(num_bin)
    return int(num_bin,2)


def main():
    data = {}
    mask = ''
    for i in instructions:
        if 'mask' in i:
            mask = i.lstrip('mask = ')
        elif 'mem' in i:
            c_num = convert(int(i.partition('=')[2].strip()),mask)
            data[i.partition('=')[0]] = c_num
    return data


print('The solution to day 14, part 1 is: {}'.format(sum(main().values())))
