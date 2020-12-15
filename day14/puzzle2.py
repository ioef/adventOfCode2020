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


def find_sum(memory):
    total = 0
    for value in memory.values():
        total += value
    return total

memory = {}
sizeof_memory = 36


for line in lines:
    cmd, value = line.split('=')
    cmd = cmd.strip()
    value = value.strip()
    if "mask" in line:
        bit_mask = value
    else:
        value = int(value)
        address = cmd[4:-1]
        #convert to int from str, bin from int, and back to str
        address = str(convert_dec_to_bin(int(address)))
        #padding with zeros up until fill the size of memory
        address = ("0" * (sizeof_memory - len(address))) + address
        masked_val = ""
        for i in range(sizeof_memory):
            if bit_mask[i] == "1":
                masked_val += "1"
            elif bit_mask[i] == "X":
                masked_val += "X"
            else:
                masked_val += address[i]

        floating_address = [""]
        for bit in masked_val:
            if bit !="X":
                for i in range(len(floating_address)):
                    floating_address[i] += bit
            else:
                temp_floating = []
                for floating in floating_address:
                    temp_floating.append(floating + "0")
                    temp_floating.append(floating + "1")
                floating_address = temp_floating

        for f in floating_address:
            memory[int(f, 2)] = value

print(find_sum(memory))
