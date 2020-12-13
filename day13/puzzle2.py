#!/usr/bin/env python3



with open("input", "r") as fileIn:
   schedules = [line.strip() for line in fileIn.readlines()]


buses = [line for line in schedules[1].split(',')]
buses = [int(valid) for valid in buses if valid !='x']

ids = []

def mod_inverse(a,n):
    # find some x such that (a*x) % n == 1
    a = a % n
    if n == 1:
        return 1
    for x in range(1, n):
        if (a*x) % n == 1:
            return x

# n busses
# bus k at index i departs at a time t+i
# t+i % k == 0
# t % k == -i
# t % k = k-i
# index = (k - (i%k)) % k
def get_earliest_time():
    ids = []
    fullProduct = 1
    for i in range(len(buses)):
        item = buses[i]
        if item != 'x':
            k = int(item)
            i = i % k
            ids.append(((k-i)%k,k))
            fullProduct *= k

    total = 0
    for i,k in ids:
        partialProduct = fullProduct // k

        inverse = mod_inverse(partialProduct,k)
        assert (inverse * partialProduct) % k == 1

        term = inverse * partialProduct * i
        total += term

    return total % fullProduct

print(get_earliest_time())
