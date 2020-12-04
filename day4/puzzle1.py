#!/usr/bin/env python3


passports = []
with open('input','r') as f:
    passports =  f.read().split('\n\n')


passPortfields = ['ecl', 'eyr', 'pid', 'hcl', 'byr', 'iyr', 'hgt']
validPassportCounter = 0

for passport in passports:
    listofValid = []
    dataFields = passport.split()
    for field in passPortfields:
        if field in passport:
            listofValid.append(True)
        else:
            listofValid.append(False)
    if all(listofValid):
        validPassportCounter += 1


print("Found %s Valid passports"%validPassportCounter)
