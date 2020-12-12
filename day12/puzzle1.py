#!/usr/bin/env python3

#Today's puzzle resembles the Game of Life

with open("input", "r") as fileIn:
   grid = [line.strip() for line in fileIn.readlines()]


#starting position
x = 0
y = 0

currentDirection = 1
for position in grid:
    direction = position[0]
    value = int(position[1:])

    if direction == "N" or (direction == "F" and currentDirection == 0):
        y += value
    elif direction == "E" or (direction == "F" and currentDirection == 1):
        x += value
    elif direction == "S" or (direction == "F" and currentDirection == 2):
        y -= value
    elif direction == "W" or (direction == "F" and currentDirection == 3):
        x -= value
    elif direction == "R":
        currentDirection += value // 90
        currentDirection %= 4
    elif direction == "L":
        currentDirection -= value // 90
        currentDirection %= 4

print("X:%s Y:%s Sum:%s"%(x,y,abs(x)+abs(y)))
