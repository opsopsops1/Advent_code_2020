with open("inputs/day10.txt") as file:
  data = [i.strip() for i in file]

h = len(data)
w = len(data[0])

# Part 1

def check(a, b):
  for i in range(h):
    for j in range(w):
      if a[i][j] != b[i][j]:
        return True
  return False

def count1(seat):
  r = 0
  for i in range(h):
    for j in range(w):
      if seat[i][j] == "#":
        r += 1
  return r

d = [["." for j in range(w)] for i in range(h)]
while check(d, data):
  d = data.copy()
  for i in range(h):
    for j in range(w):
      if d[i][j] == ".":
        continue
      c = 0
      for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
          if di == 0 and dj == 0:
            continue
          if i+di < 0 or i+di >= h:
            continue
          if j+dj < 0 or j+dj >= w:
            continue
          if d[i+di][j+dj] == "#":
            c += 1
      if d[i][j] == "L" and c == 0:
        l = list(d[i])
        l[j] = "#"
        data[i] = "".join(l)
      if d[i][j] == "#" and c >= 4:
        l = list(d[i])
        l[j] = "L"
        data[i] = "".join(l)
  print(data[0])

print(count1(data))
# Part 2