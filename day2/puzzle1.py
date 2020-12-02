#!/usr/bin/env python3
import re




passwordFile = []
with open('input','r') as f:
    passwordFile = f.read().split('\n')

#remove last empty index
passwordFile = passwordFile[:-1]



def validate_password(char, policy, text):
    print("Policy under check:%s for character %s"%(policy, character))
    start = int(policy.split('-')[0])
    stop = int(policy.split('-')[1])

    count =0
    for c in text:
        if char == c:
            count +=1
    if count>=start and count<=stop:
        return True
    else:
        return False

count = 0
for record in passwordFile:
    policy = record.split(':')[0].split(' ')[0]
    character  = record.split(':')[0].split(' ')[1]
    text = record.split(':')[1]

    if validate_password(character, policy, text):
        count += 1


print(f"Count {count}")
