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
numberofRows= len(roadMap)
x = 1
yAxisCounter = 2
for i in range(len(roadMap)):
    print(yAxisCounter, x)
    if roadMap[yAxisCounter][x] == "#":
           treeCounter += 1
    yAxisCounter = (yAxisCounter + 2)%numberofRows
    x = (x + 1)%numberOfColumns

print("Encountered number of %s trees" %treeCounter)
