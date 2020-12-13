#!/usr/bin/env python3


with open("input", "r") as fileIn:
   schedules = [line.strip() for line in fileIn.readlines()]


my_arrival = int(schedules[0])
schedules = [line for line in schedules[1].split(',')]
schedules = [int(valid) for valid in schedules if valid !='x']


compare_list = []

k = 0
for value in schedules:
    final_value = 0
    compare_list.append([])
    #populate the first 100000 values
    for i in range(100000):
        final_value += value
        compare_list[k].append(int(final_value))
    k += 1


for row in compare_list:
    value = min(row, key=lambda x:abs(x-my_arrival))
    if value >= my_arrival:
        print(row[0])
        difference = (value - my_arrival)
        print("Id of BUS multiplied by difference: %d"%(difference * row[0]))
        break
