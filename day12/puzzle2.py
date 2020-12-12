#!/usr/bin/env python3

with open("input", "r") as fileIn:
   grid = [line.strip() for line in fileIn.readlines()]


#starting position
x = 0
y = 0

i = 10
j = 1


for position in grid:
    direction = position[0]
    value = int(position[1:])

    if direction == "N":
        j +=value
    elif direction == "E":
        i += value
    elif direction == "S":
        j -= value
    elif direction == "W":
        i -= value
    elif direction == "R":
        while value>0:
            #y becomes x
            i1 = j
            #x becomes -y
            j1 = -1 * i
            #set new x and new y
            i,j = i1, j1
            value -= 90
    elif direction == "L":
        while value>0:
            #-y becomes x
            i1 = -1 * j
            #x becomes y
            j1 = i
            #set new x and new y
            i,j = i1, j1
            value -= 90
    elif direction == "F":
        x += value * i
        y += value * j

print("X:%s Y:%s Sum:%s"%(x,y,abs(x)+abs(y)))
