with open("inputs/day10.txt") as file:
  data = [int(i) for i in file]

data.sort()

# Part 1
def part1():
  d = [0]*4
  p = 0
  for i in data:
    d[i-p] += 1
    p = i
  return d[1]*(d[3]+1)

print(part1())

# Part 2
def part2():
  pass
