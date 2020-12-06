#!/bin/env python3

answers = []

with open('input', 'r') as f:
    for line in f.readlines():
       answers.append(line.strip())

answers.append('')

groups = []
cumulative = ""
currentSet = {""}

intList = []
for answer in answers:
    if answer != '':
        intList.append(set(answer))
    else:
        groups.append(intList)
        intList = []
sum = 0
for group in groups:
    sum += len(set.intersection(*group))

print(sum)
