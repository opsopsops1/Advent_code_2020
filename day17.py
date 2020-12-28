with open("inputs/day17.txt") as file:
  data = [line.strip() for line in file]

d = [-1, 0, 1]
s = set()
for x, line in enumerate(data):
  for y, c in enumerate(line):
    if c == "#":
      s.add((x, y, 0))

# Part 1
def part1(actived):
  for _ in range(6):
    mark = {}
    for x, y, z in actived:
      for xi in d:
        for yi in d:
          for zi in d:
            if xi == yi == zi == 0:
              continue
            mark[(x+xi, y+yi, z+zi)] = mark.get((x+xi, y+yi, z+zi), 0) + 1
    new_actived = set()
    for k, v in mark.items():
      if v == 3:
        new_actived.add(k)
      elif v == 2 and k in actived:
        new_actived.add(k)
    actived = new_actived
  return len(actived)

print(part1(s))

# Part 2
def part2(actived):
  for _ in range(6):
    mark = {}
    for x, y, z, w in actived:
      for xi in d:
        for yi in d:
          for zi in d:
            for wi in d:
              if xi == yi == zi == wi == 0:
                continue
              mark[(x+xi, y+yi, z+zi, w+wi)] = mark.get((x+xi, y+yi, z+zi, w+wi), 0) + 1
    new_actived = set()
    for k, v in mark.items():
      if v == 3:
        new_actived.add(k)
      elif v == 2 and k in actived:
        new_actived.add(k)
    actived = new_actived
  return len(actived)

s2 = set()
for t in s:
  s2.add((t[0], t[1], t[2], 0))

print(part2(s2))