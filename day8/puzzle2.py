#!/usr/bin/env python3

with open("input", "r") as fileInput:
    lines = fileInput.readlines()
    program = [line.strip() for line in lines]

cmds = [ cmd.split() for cmd in program  ]


def find_eof():
    acc = 0
    cmdIndex = 0
    cmdsExecuted = []
    alreadySeen  = set()
    while cmdIndex < len(cmds):
        cmd = cmds[cmdIndex][0]
        value = cmds[cmdIndex][1]
        cmd_to_add = cmd + value + str(cmdIndex)
        if cmd_to_add in alreadySeen:
            return acc, False
        alreadySeen.add(cmd_to_add)
        print("Current Position of cmdIndex:%s command executed:%s %s"%(cmdIndex,
         cmds[cmdIndex][0].upper(), cmds[cmdIndex][1]))
        if cmd == "acc":
            acc += int(cmds[cmdIndex][1])
            cmdIndex += 1
        if cmd == "jmp":
            cmdIndex = cmdIndex + (int(cmds[cmdIndex][1]))
        if cmd == "nop":
            cmdIndex += 1
        cmdsExecuted.append(cmd)
    return acc, True

index = 0
while index < len(cmds):
    if cmds[index][0] == 'jmp':
        print("Changing Index %s"%index)
        cmds[index][0] = 'nop'
        acc, result = find_eof()

        print(acc)
        if result:
            print("Accumulator:%s"%acc)
            break
        else:
            if cmds[index][0] == 'nop':
                cmds[index][0] = 'jmp'
    index +=1
