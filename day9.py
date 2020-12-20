with open("inputs/day9.txt") as file:
  data = [int(i) for i in file]

# Part 1
part1 = 0
ok = True
for i in range(25, len(data)):
  sort_data = sorted(data[i-25:i])

  r = 24
  for l in range(24):
    while r > 0 and sort_data[l]+sort_data[r] > data[i]:
      r -= 1
    if sort_data[l]+sort_data[r] == data[i]:
      break
    if l >= r:
      ok = False
      break

  if not ok:
    part1 = data[i]
    break

print(part1)

# Part 2
def part2():
  for i in range(len(data)):
    for j in range(i+2, len(data)):
      s = sum(data[i:j])
      if s == part1:
        return min(data[i:j]) + max(data[i:j])

print(part2())
