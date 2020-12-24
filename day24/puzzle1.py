#!/usr/bin/env python3

with open("input", "r") as fileIn:
    lines = [line.strip() for line in fileIn.readlines()]

tileSet = set()
for line in lines:
    x,y,z = 0,0,0
    while line:
        if line.startswith('e'):
            x += 1
            y -= 1
            line = line[1:]
        elif line.startswith('ne'):
            x += 1
            z -= 1
            line = line[2:]
        elif line.startswith('se'):
            y -= 1
            z += 1
            line = line[2:]
        elif line.startswith('w'):
            x -= 1
            y += 1
            line = line[1:]
        elif line.startswith('nw'):
            z -= 1
            y += 1
            line = line[2:]
        elif line.startswith('sw'):
            x -= 1
            z += 1
            line = line[2:]
        else:
            assert False
    if (x,y,z) in tileSet:
        tileSet.remove((x,y,z))
    else:
        tileSet.add((x,y,z))
print(f'Tiles left in black side up: {len(tileSet)}')
