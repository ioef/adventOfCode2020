#!/usr/bin/env python3


roadMap = []
with open('input','r') as f:
    roadMap = f.read().split('\n')

roadMap = roadMap[:-1]

#create a two dimensional array from the list
roadMap = [ list(line) for line in roadMap]


treeCounter = 0
yAxisCounter = 0

numberOfColumns = len(roadMap[0])
for i in range(0, len(roadMap)):
    if roadMap[i][yAxisCounter] == "#":
           treeCounter += 1
    yAxisCounter = (yAxisCounter + 3)%numberOfColumns

print("Encountered number of %s trees" %treeCounter)
