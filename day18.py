import re
with open("inputs/day18.txt") as file:
  data = [line.strip() for line in file]

findp = re.compile(r"\(([^()]+)\)")

def compute_value(s: str) -> int:
  parts = s.split()
  v = int(parts[0])
  i = 1
  while i < len(parts):
    op = parts[i]
    n = int(parts[i+1])
    if op == "+":
      v += n
    elif op == "*":
      v *= n
    else:
      raise AssertionError(op)
    i += 2
  return v

# Part 1
part1 = 0
for line in data:
  line_cp = line[:]
  while findp.search(line_cp):
    line_cp = findp.sub(lambda match: str(compute_value(match[1])), line_cp)
  part1 += compute_value(line_cp)

print(part1)

# Part 2

def func(match):
  return str(int(match[1])+int(match[2]))

findpp = re.compile(r"(\d+) \+ (\d+)")
def compute_value2(s: str) -> int:
  print(s)
  while findpp.search(s):
    s = findpp.sub(func, s)
    print(s)
  parts = s.split()
  v = int(parts[0])
  i = 1
  while i < len(parts):
    v *= int(parts[i+1])
    i += 2
  return v

part2 = 0
for line in data:
  line_cp = line[:]
  while findp.search(line_cp):
    line_cp = findp.sub(lambda match: str(compute_value2(match[1])), line_cp)
  part2 += compute_value2(line_cp)

print(part2)