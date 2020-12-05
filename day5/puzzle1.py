#!/bin/env python3

boardingPasses = []

with open('input', 'r') as f:
  boardingPasses = [ line.strip() for line in f.readlines() ]

listofIds = []
for boardingPass in boardingPasses:
    rows = boardingPass[0:7]
    columns = boardingPass[7:]

    rowBits = []
    for char in rows:
        if char == 'F':
            rowBits.append('0')
        else:
            rowBits.append('1')
    row = int(''.join(rowBits), 2)

    colBits = []
    for char in columns:
        if char == 'L':
            colBits.append('0')
        else:
            colBits.append('1')
    col = int(''.join(colBits), 2)

    print(row, col)
    listofIds.append(row *8 + col)

print(max(listofIds))
