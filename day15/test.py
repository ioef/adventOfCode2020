data = [2,1,3]

def play_memory_game(size):
    mem = {}

    mem  = {number:idx for idx,number in enumerate(data)}

    for i in range(len(data)-1,size-1):
        num = data[i]

        if num not in mem:
            data.append(0)
            mem[num] = i

        else:
            j = mem[num]
            newNum = i - j
            data.append(newNum)
            mem[num] = i
        print(data)
    return data[-1]

print(play_memory_game(2020))
