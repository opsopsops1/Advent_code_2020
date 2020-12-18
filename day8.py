# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:35:43 2020

@author: user
"""

with open("inputs/day8.txt") as file:
    data = [line.strip() for line in file]

def part1(data_command):
    i = 0
    res = 0
    command_set = set()
    while 1:
        if i in command_set:
            break
        if i == len(data_command):
            return (res, True)
        command_set.add(i)
        command = data_command[i].split()
        if command[0] == "nop":
            pass
        elif command[0] == "acc":
            res += int(command[1][1:]) * (1 if command[1][0] == '+' else -1)
        else:
            i += int(command[1][1:]) * (1 if command[1][0] == '+' else -1)
            continue
        i += 1
    return (res, False)


# Part 1

print(part1(data)[0])


# Part 2

def part2():
    for i in range(len(data)):
        if data[i][:3] == "acc":
            continue
        data_cp = data.copy()
        if data_cp[i][:3] == "nop":
            data_cp[i] = data_cp[i].replace("nop", "jmp")
        else:
            data_cp[i] = data_cp[i].replace("jmp", "nop")
        res1, res2 = part1(data_cp)
        if res2:
            return(res1)

print(part2())