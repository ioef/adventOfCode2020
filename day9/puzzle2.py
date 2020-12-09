#!/usr/bin/env python3

with open("input", "r") as fileIn:
    sequence = [int(line.strip()) for line in fileIn.readlines()]

for i in range(len(sequence)):
    summary = 0
    for j in range(i, len(sequence)):
        summary += sequence[j]
        if summary == 177777905:
            finalList = sequence[i:j+1]
            finalList.sort()
            if len(finalList) > 1:
                minimum = finalList[0]
                maximum = finalList[-1]
                finalsum = minimum + maximum
                print("List :%s",finalList)
                print("Sum of Min + Max:%s"%finalsum)
