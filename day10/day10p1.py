
def p1():
    data = sorted([int(line.strip()) for line in open('input.txt','rt')])
    previous_value, one_jolt_adapters, three_jolt_adapters = 0,0,0
    for idx,val in enumerate(data):
        if val - previous_value == 1:
            one_jolt_adapters += 1
        elif val - previous_value == 3:
            three_jolt_adapters += 1
        previous_value = val
    three_jolt_adapters += 1
    return one_jolt_adapters * three_jolt_adapters

print('The solution to part 1 is: {}'.format(p1()))

