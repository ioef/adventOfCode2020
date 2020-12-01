#!/bin/env python3
import sys

fileContents = []
with open('input','r') as f:
    fileContents = f.read().split('\n')


for i in range(len(fileContents)-1):
    for j in range(i+1, len(fileContents)-1):
        for k in range(j+1, len(fileContents)-1):
            print(i,j,k)
            print(fileContents[i], fileContents[j], fileContents[k]) 
            if int(fileContents[i]) + int(fileContents[j]) \
                    + int(fileContents[k]) == 2020:
                print("=====================")
                print(fileContents[i])
                print(fileContents[j])
                print(fileContents[k])
                mul = int(fileContents[i]) * int(fileContents[j]) \
                * int(fileContents[k])
                print(mul)
                print("Found!")
                sys.exit()
