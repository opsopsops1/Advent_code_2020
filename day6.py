with open("inputs/day6.txt") as file:
  data = file.read().split("\n\n")

# Part 1
part1 = 0
for para in data:
  cnt = set()
  for line in para:
    for c in line.strip():
      cnt.add(c)
  part1 += len(cnt)

print(part1)

# Part 2
part2 = 0
for para in data:
  cnt = {}
  for line in para:
    l = set()
    for c in line.strip():
      l.add(c)
    for c in l:
      cnt[c] = cnt.get(c, 0) + 1
  for k, v in cnt.items():
    if v == len(para.split()):
      part2 += 1

print(part2)