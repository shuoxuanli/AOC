import sys

notes = sys.stdin.read().split("\n\n")

x, y = 0, 0
for g in notes:
	g = g.split("\n")
	n, m = len(g), len(g[0])
	for i in range(n - 1):
		ok = True
		for j in range(m):
			l, r = i, i + 1
			while l >= 0 and r < n and ok:
				ok = ok and g[l][j] == g[r][j]
				l -= 1
				r += 1
		if ok: x += i + 1

	for i in range(m - 1):
		ok = True
		for j in range(n):
			l, r = i, i + 1
			while l >= 0 and r < m and ok:
				ok = ok and g[j][l] == g[j][r]
				l -= 1
				r += 1
		if ok: y += i + 1

print(x * 100 + y)
