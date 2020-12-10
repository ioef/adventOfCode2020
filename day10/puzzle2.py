#!/usr/bin/env python3

with open("input", "r") as fileIn:
    jolts = [int(line.strip()) for line in fileIn.readlines()]


jolts.sort()

jolts = [0] + jolts
jolts.append(jolts[-1]+3)


newjolts = [1]
for i in range(1, len(jolts)):
    result = 0
    for j in range(i):
        if jolts[j] + 3 >= jolts[i]:
            result += newjolts[j]
    newjolts.append(result)

print("Total number of distinct ways to connect chrg. outlet: %s"%max(newjolts))
