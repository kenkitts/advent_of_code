"""Solution for day 4, part 1 puzzle on aventofcode.com"""

with open(file='input.txt',mode='rt',encoding='utf-8',newline='\n') as file: # Open input file for reading
    file_list = file.read().split('\n\n')
    file_list_curated = []
    passport_data = []
    for item in file_list:
        file_list_curated.append(item.replace('\n',' '))
    for item in file_list_curated:
        x = item.split()
        dictionary_temp = {}
        for key_value in x:
            key_value = key_value.split(':')
            key = key_value[0]
            value = key_value[1]
            dictionary_temp.update({key:value})
        passport_data.append(dictionary_temp)

valid_passports = 0

def passport_check(p_data):
    x = p_data.keys()
    if ('byr' in x and
        'iyr' in x and
        'eyr' in x and
        'hgt' in x and
        'hcl' in x and
        'ecl' in x and
        'pid' in x):
        return True
    else:
        return False

for item in passport_data:
    if passport_check(item) is True:
        valid_passports += 1

print(valid_passports)