# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:41:37 2020

@author: user
"""

with open("inputs/day15.txt") as file:
    data = [int(i.strip()) for i in file.read().split(",")]

def play(num):
    spoken = 0
    rep = {}
    for i in range(num):
        if i < len(data):
            spoken = data[i]
            rep[spoken] = [i]
            continue
        if len(rep[spoken]) == 1:
            # new
            spoken = 0
        else:
            # old
            r = rep[spoken]
            spoken = r[-1] - r[-2]
        if rep.get(spoken) == None:
            rep[spoken] = []
        rep[spoken].append(i)
        if i%1000000 == 0:
            print(spoken)
    print(spoken)

# Part 1
play(2020)
# Part 2
play(30000000)