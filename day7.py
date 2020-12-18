# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:43:16 2020

@author: user
"""

with open("inputs/day7.txt") as file:
    data = [line.replace(".", "") for line in file]

bags = {}

for line in data:
    line = line.replace("bags", "").replace("bag", "").strip()
    line = line.split("contain")
    outer_color = line[0].strip()
    inner_color = line[1].strip()
    
    bags[outer_color] = []
    
    for color_e in inner_color.split(","):
        if color_e == "no other":
            continue
        color_e2 = color_e.strip()
        count = int(color_e2[0])
        color = color_e2[2:]
        bags[outer_color].append((color.strip(), count))

def check(bag_color):
    for inner_bag in bags[bag_color]:
        if inner_bag[0] in gold_set or inner_bag[0] == "shiny gold":
            gold_set.add(bag_color)
            return True
        if check(inner_bag[0]):
            return True

def dig(bag_color):
    cnt = 0
    # if bags.get(bag_
    for inner_color in bags[bag_color]:
        cnt += (inner_color[1]) * (dig(inner_color[0])+1)
    
    
    return cnt



# Part 1

gold_set = set()
part1 = 0

for bag in bags:
    if check(bag):
        part1 += 1

print(part1)


# Part 2

part2 = dig("shiny gold")

print(part2)