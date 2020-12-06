#!/bin/env python3

answers = []

with open('input', 'r') as f:
    for line in f.readlines():
       answers.append(line.strip())

answers.append('')

groups = []
cumulative = ""
sums = 0 
for answer in answers:
    if answer != '':
        cumulative += answer
    else:
        groups.append(set(cumulative))
        sums += len(set(cumulative))
        cumulative = ""

print(sums)
