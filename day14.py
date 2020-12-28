with open("inputs/day14.txt") as file:
  data = [line.replace("[", " ").replace("]", "").replace("=", "").strip() for line in file]

print(data[0])

# Part 1
def part1():
  mem = {}
  for line in data:
    if line[:4] == "mask":
      mask = line[6:][::-1]
      continue
    l = line.split()
    b = list("{0:b}".format(int(l[2]))[::-1])
    b = b + ["0"]*(36-len(b))
    # print(b)
    for i in range(36):
      if mask[i] != "X":
        b[i] = mask[i]
    mem[l[1]] = "".join(b[::-1])
  r = 0
  for v in mem.values():
    r += int(v, 2)
  print(r)

part1()