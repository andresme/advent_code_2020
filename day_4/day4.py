import re

hcl_regex = re.compile(r'#[0-9a-f]{6}')
ecl_regex = re.compile(r'amb|blu|brn|gry|grn|hzl|oth')
pid_regex = re.compile(r'^[0-9]{9}$')

def count_valid_passports(passports, required_fields, validations=None):
    valid_passports = 0
    for i in passports:
        if is_valid(i, required_fields, validations):
            valid_passports = valid_passports + 1
    return valid_passports

def is_valid(passport, required_fields, validations):
    for i in required_fields:
        if i not in passport:
            return False
        if validations and not validations[i](passport[i]):
            return False
    return True

if __name__ == "__main__":
    passports = []
    passport = {}
    with open('day_4/input.txt', 'r') as inputFile:
        for line in inputFile.readlines():
            if line == '\n':
                passports.append(passport)
                passport = {}
                continue
            parts = line.split(' ')
            for part in parts:
                part = part.split(':')
                passport[part[0].strip()] = part[1].replace('\n', '')
        
    
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    validations = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: (150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' 
                            else 59 <= int(x[:-2]) <= 76 if x[-2:] == 'in' else False),
        'hcl': lambda x: bool(re.match(hcl_regex, x)),
        'ecl': lambda x: bool(re.match(ecl_regex, x)),
        'pid': lambda x: bool(re.match(pid_regex, x))
    }

    print(f'valid_passports 1: {count_valid_passports(passports, required_fields)}')
    print(f'valid_passports 2: {count_valid_passports(passports, required_fields, validations)}')

