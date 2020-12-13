#!/usr/bin/env python3

#Another solution, taken from Jonathan Paulson
#https://www.youtube.com/watch?v=x40aLK9KjYQ

with open("input", "r") as fileIn:
   schedules = [line.strip() for line in fileIn.readlines()]


t0 = int(schedules[0])
schedules = [line for line in schedules[1].split(',')]
schedules = [int(valid) for valid in schedules if valid !='x']


best = None

for b in schedules:
    t = t0
    while t%b !=0:
        t += 1
    score = t-t0
    if best is None or score < best[0]:
        best = (score, b)
print(best[0]*best[1])

