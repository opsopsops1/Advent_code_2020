with open("inputs/day11.txt") as file:
  data = [i.strip() for i in file]

h = len(data)
w = len(data[0])
data2 = data[:]

def check(a, b):
  for i in range(h):
    for j in range(w):
      if a[i][j] != b[i][j]:
        return True
  return False

def count(seat):
  r = 0
  for i in range(h):
    for j in range(w):
      if seat[i][j] == "#":
        r += 1
  return r

# Part 1
d = ["." * w] * h
while check(d, data):
  d = data[:]
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
        l = list(data[i])
        l[j] = "#"
        data[i] = "".join(l)
      if d[i][j] == "#" and c >= 4:
        l = list(data[i])
        l[j] = "L"
        data[i] = "".join(l)

print(count(data))

# Part 2

d = ["." * w] * h
di = [1, 1, 1, 0, 0, -1, -1, -1]
dj = [1, 0, -1, 1, -1, 1, 0, -1]
while check(d, data2):
  d = data2[:]
  for i in range(h):
    for j in range(w):
      if d[i][j] == ".":
        continue
      c = 0
      for k in range(8):
        for m in range(1, 2*len(data2)):
          ii = i + m*di[k]
          jj = j + m*dj[k]
          if ii < 0 or ii >= h or jj < 0 or jj >= w:
            break
          if d[ii][jj] == "L":
            break
          if d[ii][jj] == "#":
            c += 1
            break
      if d[i][j] == "L" and c == 0:
        l = list(data2[i])
        l[j] = "#"
        data2[i] = "".join(l)
      if d[i][j] == "#" and c >= 5:
        l = list(data2[i])
        l[j] = "L"
        data2[i] = "".join(l)

print(count(data2))