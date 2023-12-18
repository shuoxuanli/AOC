import sys

lines = sys.stdin.read().split("\n")

l = [1] * len(lines)
for i, line in enumerate(lines):
	line = line.split(": ")[1]
	a, b = line.split("|")
	a, b = a.split(), b.split()
	s = sum(x in a for x in b)
	for j in range(1, s + 1):
		l[i + j] += l[i]

print(sum(l))
