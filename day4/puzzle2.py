#!/usr/bin/env python3


passports = []
with open('input','r') as f:
    passports =  f.read().split('\n\n')


passPortfields = ['ecl', 'eyr', 'pid', 'hcl', 'byr', 'iyr', 'hgt']
validPassportCounter = 0
def validate(data_field):
    key = data_field.split(':')[0]
    value = data_field.split(':')[1]
    if key == "byr" and len(value) == 4:
        if int(value) >=1920 and int(value) <=2002:
            return True
    if key == "iyr" and len(value) == 4:
        if int(value) >=2010 and int(value) <=2020:
            return True
    if key == "eyr" and len(value) == 4:
        if int(value) >=2020 and int(value) <=2030:
            return True
    if key == "hgt":
        if value.endswith('cm'):
            numerical = int(value.split('cm')[0])
            if numerical>=150 and numerical<=193:
                return True
        if value.endswith('in'):
            numerical = int(value.split('in')[0])
            if numerical>=59 and numerical<=76:
                return True
    if key == "hcl":
        if value.startswith('#'):
            if len(value) == 7 and value.lstrip('#').isalnum():
                return True
    if key == "ecl":
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    if key == "pid":
        if len(value)==9 and value.isnumeric():
            return True
    if key == "cid":
        return True
    return False

for passport in passports:
    listofValid = []
    for field in passPortfields:
        if field in passport:
            listofValid.append(True)
        else:
            listofValid.append(False)
    #Now let's check for the contents
    if all(listofValid):
        dataFields = passport.split()
        finaListofValid = []
        for field in dataFields:
            if validate(field):
                finaListofValid.append(True)
            else:
                finaListofValid.append(False)
        if all(finaListofValid):
            validPassportCounter += 1


print("Found %s Valid passports"%validPassportCounter)
