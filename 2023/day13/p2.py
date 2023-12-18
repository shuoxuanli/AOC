import sys

notes = sys.stdin.read().split("\n\n")

x, y = 0, 0
for g in notes:
	g = g.split("\n")
	n, m = len(g), len(g[0])
	for i in range(n - 1):
		diff = 0
		for j in range(m):
			l, r = i, i + 1
			while l >= 0 and r < n:
				diff += g[l][j] != g[r][j]
				l -= 1
				r += 1
		if diff == 1: x += i + 1

	for i in range(m - 1):
		diff = 0
		for j in range(n):
			l, r = i, i + 1
			while l >= 0 and r < m:
				diff += g[j][l] != g[j][r]
				l -= 1
				r += 1
		if diff == 1: y += i + 1

print(x * 100 + y)
