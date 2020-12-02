#!/usr/bin/env python3
import re


passwordFile = []
with open('input','r') as f:
    passwordFile = f.read().split('\n')

#remove last empty index
passwordFile = passwordFile[:-1]

def findAll(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def validate_password(char, policy, text):
    first = int(policy.split('-')[0])
    second = int(policy.split('-')[1])
    indices_of_char = findAll(text, char)

    print("First:%s"%first)
    print("Second:%s"%second)

    print("Policy under check:%s for character %s"%(policy, char))
    print("Text:%s"%text)
    if int(first) in indices_of_char and int(second) not in indices_of_char:
        return True
    elif int(first) not in indices_of_char and int(second) in indices_of_char:
        return True
    else:
        return False

count = 0
for record in passwordFile:
    policy = record.split(':')[0].split(' ')[0]
    character = record.split(':')[0].split(' ')[1]
    text = record.split(':')[1]

    if validate_password(character, policy, text):
        count += 1


print("Count:%s"%count)
