#!/usr/bin/env python3

with open("input", "r") as fileIn:
    lines = [line.strip() for line in fileIn.readlines()]


def convert_dec_to_bin(number):
    if number < 0:
        print("Must be a positive integer")
        return None
    if number == 0:
        return '0'
    else:
        return convert_dec_to_bin(number//2) + str(number%2)

def convert_bin_to_dec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

def find_sum(memory):
    total = 0
    for value in memory.values():
        total += value
    return total



memory = {}

for line in lines:
    cmd, value = line.split('=')
    cmd = cmd.strip()
    value = value.strip()
    if "mask" in line:
        bit_mask = value
    else:
        value = int(value)
        mem_location = cmd[4:-1]
        binary_value = convert_dec_to_bin(value)
        while len(binary_value) < 36:
            binary_value = '0' + binary_value
        binary_value = list(binary_value)
        for i in range(len(bit_mask)):
            if bit_mask[i] !='X':
                binary_value[i] = bit_mask[i]
        memory[mem_location] = convert_bin_to_dec(binary_value)


print("Total Sum: %s"%find_sum(memory))
