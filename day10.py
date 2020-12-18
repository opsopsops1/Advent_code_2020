with open("day10.txt") as file:
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
      if data[i][j] == ".":
        continue

  print("OK")
  break

print(count1(data))
# Part 2