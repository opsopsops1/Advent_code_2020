with open("inputs/day20.txt") as file:
  data = [para.strip() for para in file.read().split("\n\n")]

print(data[0])

# Part 1
def part1(data):
  g = {}
  tile = {}
  for para in data:
    p = para.splitlines()
    g[p[0][5:9]] = [p[1], p[-1][::-1]]
    s1 = ""
    s2 = ""
    for i in range(1, len(p)):
      s1 += p[len(p)-i][0]
      s2 += p[i][-1]
    g[p[0][5:9]].extend([s1, s2])
    tile[p[0][5:9]] = 0

  for k, v in g.items():
    for i in v:
      for other, edge in g.items():
        if k == other:
          continue
        if i in edge or i[::-1] in edge:
          tile[k] += 1
  r = 1
  for k, v in tile.items():
    if v == 2:
      r *= int(k)
  return r

print(part1(data))