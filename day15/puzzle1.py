#!/usr/bin/env python3
#Today's puzzle is Van eck's sequence


def van_eck_sequence(end):
    seen = [6,3,15,13,1,0]
    n = len(seen)-1

    #number location
    location = {number:idx for idx,number in enumerate(seen)}
    while n < end-1:
        val = seen[n]
        if val in location.keys():
            position = location[val]
            newval = n - position
            seen.append(newval)
            location[val] = n
        else:
            seen.append(0)
            location[val] = n
        n += 1
    return seen[-1]

print("Part1:%s"%van_eck_sequence(2020))
print("Part1:%s"%van_eck_sequence(30000000))
