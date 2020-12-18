# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:40:08 2020

@author: user
"""
import math

with open("inputs/day13.txt") as file:
    data = [line.strip() for line in file]


time = int(data[0])

busid = [int(num) for num in data[1].split(",") if num != "x"]

# Part 1

def part1():
    res = 0
    mi = max(busid)**2
    for id in busid:
        if time%id == 0:
            return 0
        m = (time//id + 1)*id - time
        if m < mi:
            mi = m
            res = m*id
    return res

print(part1())

# Part 2

busid_r = [(int(num), r) for r, num in enumerate(data[1].split(",")) if num.isnumeric()]

def part2():
    def find(r, a, b):
        while 1:
            if (r+b[1]) % b[0] == 0:
                return r, a*b[0]
            r += a
    acc = 1
    res = busid_r[0][0]
    for bus in busid_r:
        res, acc = find(res, acc, bus)
    return res

print(part2())