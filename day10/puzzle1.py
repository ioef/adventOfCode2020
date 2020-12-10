#!/usr/bin/env python3

with open("input", "r") as fileIn:
    jolts = [int(line.strip()) for line in fileIn.readlines()]


jolts.sort()

jolts = [0] + jolts
jolts.append(max(jolts)*3)

count_diff_of_ones = 0
count_diff_of_threes = 0
for i in range(0, len(jolts)-1):
        diff = jolts[i+1] - jolts[i]

        if diff == 1:
            count_diff_of_ones += 1
        elif diff == 3:
            count_diff_of_threes += 1


print(count_diff_of_ones, count_diff_of_threes)
print(count_diff_of_ones * count_diff_of_threes)
