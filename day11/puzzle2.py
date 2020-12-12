#!/usr/bin/env python3

#Today's puzzle resembles the Game of Life

with open("input", "r") as fileIn:
    layout = [line.strip() for line in fileIn.readlines()]

def populate_offsets():
    offsetList = []
    tempList = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            tempList = [i,j]
            if i==0 and j==0:
                continue
            offsetList.append(tempList)
    return offsetList

def count_adjacent_occuppied(table, row, col):
    total = 0
    offsets = populate_offsets()
    for x in offsets:
        dx = row + x[0]
        dy = col + x[1]
        while dx >=0 and dx < len(table) and dy >=0 and dy < len(table[col]) \
                and table[dx][dy] =='.':
                    dx += x[0]
                    dy += x[1]
        if dx >= 0 and dx < len(table) and dy >= 0 and dy < len(table[col]):
            total += (table[dx][dy] == "#")
    return total

def totalOccupants(table):
    total = 0
    for i in table:
        total += i.count("#")
    return total

for generations in range(100):
    nextLine = []
    for row in range(len(layout)):
        rowList = ""
        for col in range(len(layout[row])):
            character = layout[row][col]
            if character != '.':
                taken_seats = count_adjacent_occuppied(layout, row, col)
                if character == "L" and taken_seats == 0:
                    character = "#"
                elif character == "#" and taken_seats >= 5:
                    character = "L"
            rowList += character
        nextLine.append(rowList)
    layout = nextLine
print(totalOccupants(layout))
