import numpy

data = numpy.loadtxt("day1.txt", dtype=int)
l_left = data[:, 0]
l_right = data[:, 1]
total = 0
for i, j in zip(sorted(l_left), sorted(l_right)):
    g, s = max(i, j), min(i, j)
    total += g - s
print(f"part1 = {total}")

total = 0
for i in l_left:
    total += i * list(l_right).count(i)
print(f"part2 = {total}")
