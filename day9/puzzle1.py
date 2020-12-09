#!/usr/bin/env python3

with open("input", "r") as fileIn:
    sequence = [int(line.strip()) for line in fileIn.readlines()]

i = 0
sums = set()

def calculate_sums(sequence, number):
    end=len(sequence)-1
    for i in range(len(sequence)):
        for j in range(end, i, -1):
            num1 = sequence[i]
            num2 = sequence[j]
            if num1 != num2 and num1 + num2 == number:
                print("Sum of %s + %s matches number"%(sequence[i], sequence[j]))
                return True
    return False

while i < len(sequence):
    curentList = sequence[i:i+25]
    if i+26 <= len(sequence):
         current_number =  int(sequence[i+25])
    if calculate_sums(curentList, current_number):
        print("Match")
    else:
        print("Number:%s"%current_number)
        print("No match!")
        break
    print('\n')
    i += 1
