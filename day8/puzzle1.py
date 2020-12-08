#!/usr/bin/env python3

with open("input", "r") as fileInput:
    lines = fileInput.readlines()
    program = [line.strip() for line in lines]


acc = 0
cmdIndex = 0

cmds = [ ]

while cmdIndex < len(program):
    cmds.append(program[cmdIndex].split())
    cmdIndex += 1


cmdIndex = 0
alreadySeen  = set()
while cmdIndex < len(cmds):
     cmd = cmds[cmdIndex][0]
     value = cmds[cmdIndex][1]
     cmd_to_add = cmd + value + str(cmdIndex)
     if cmd_to_add in alreadySeen:
         break
     alreadySeen.add(cmd_to_add)
     print("Value of ACC:%s"%acc)
     print("Current Position of cmdIndex:%s command executed:%s %s"%(cmdIndex,
         cmds[cmdIndex][0].upper(), cmds[cmdIndex][1]))
     if cmd == "acc":
         acc += int(cmds[cmdIndex][1])
         cmdIndex += 1
     if cmd == "jmp":
         cmdIndex = cmdIndex + (int(cmds[cmdIndex][1])) 
     if cmd == "nop":
         cmdIndex += 1
         pass
     steps = cmds[cmdIndex][1]
