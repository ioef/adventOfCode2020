#!/usr/bin/env python3


roadMap = []
with open('input','r') as f:
    roadMap = f.read().split('\n')

roadMap = roadMap[:-1]

#create a two dimensional array from the list
roadMap = [ list(line) for line in roadMap]

numberOfColumns = len(roadMap[0])

def treesCounter(roadMap, movement):
    treeCounter = 0
    movementsCounter = 0
    xCounterOffset = 0
    yCounterOffset =0
    xCounter = 0
    yCounter = 0
    movements = [(1,1), (1,3), (1,5), (1,7), (2,1)]

    xCounterOffset = movements[movement][0]
    yCounterOffset = movements[movement][1]
    while xCounter < len(roadMap):
        if roadMap[xCounter][yCounter] == "#":
            treeCounter += 1
        xCounter = (xCounter + xCounterOffset)
        yCounter = (yCounter + yCounterOffset)%numberOfColumns
    return treeCounter


mulCounter = 1
for i in range(0,5):
    treeCounter = treesCounter(roadMap, i)
    print("Encountered number of %s trees" %treeCounter)

    mulCounter *= treeCounter


print("Product of Multiplication %s"%mulCounter)


