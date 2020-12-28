with open("inputs/day16.txt") as file:
  data = [line.strip() for line in file]

# print(data)

p = 0
part1 = 0
inv = []
for line in data:
  if line == "":
    p += 1
  elif p == 0:
    s = line.split(": ")[1].split(" or ")
    inv.append(tuple(map(int, s[0].split("-"))))
    inv.append(tuple(map(int, s[1].split("-"))))
  elif p == 1:
    pass
  elif p == 2:
    if line[0].isalpha():
      continue
    for i in map(int, line.split(",")):
      found = False
      for t in inv:
        if t[0] <= i and i <= t[1]:
          found = True
          break
      if not found:
        part1 += i

print(part1)


