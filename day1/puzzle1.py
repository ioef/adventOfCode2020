#!/bin/env python3
import sys

fileContents = []
with open('input','r') as f:
    fileContents = f.read().split('\n')

end=len(fileContents)-2
for i in range(len(fileContents)):
    for j in range(end, i, -1):
        if int(fileContents[i]) + int(fileContents[j]) == 2020:
            print(fileContents[i])
            print(fileContents[j])
            mul = int(fileContents[i]) * int(fileContents[j])
            print(mul)
            print("Found!")
            sys.exit()
