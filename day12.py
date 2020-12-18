# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:55:05 2020

@author: user
"""

with open("inputs/day12.txt") as file:
    data = [line.strip() for line in file]



# Part 1
def part1():
    d = ["E", "S", "W", "N"]
    pos = {"E": 0, "S": 0, "W": 0, "N": 0}
    i = 0
    for s in data:
        if s[0] == "L":
            i = (i+4-int(s[1:])//90)%4
        elif s[0] == "R":
            i = (i+int(s[1:])//90)%4
        elif s[0] == "F":
            pos[d[i]] += int(s[1:])
        else:
            pos[s[0]] += int(s[1:])
    return (abs(pos["E"]-pos["W"]) + abs(pos["S"]-pos["N"]))

print(part1())

# Part 2
def part2():
    def rotate(w, a):
        if a == 0:
            return w
        if a == 2 or a == -2:
            return [w[2], w[3], w[0], w[1]]
        if a == 1 or a == -3:
            return [w[3], w[0], w[1], w[2]]
        if a == 3 or a == -1:
            return [w[1], w[2], w[3], w[0]]
    
    d = {"E": 0, "S": 1, "W": 2, "N": 3}
    way = [10, 0, 0, 1]
    shop = [0] * 4
    for s in data:
        if s[0] == "L":
            way = rotate(way, -1*(int(s[1:])//90))
        elif s[0] == "R":
            way = rotate(way, (int(s[1:])//90))
        elif s[0] == "F":
            for i in range(4):
                shop[i] += way[i]*int(s[1:])
        else:
            way[d[s[0]]] += int(s[1:])
            
    return abs(shop[0]-shop[2]) + abs(shop[1]-shop[3])

print(part2())