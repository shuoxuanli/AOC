import sys

g = sys.stdin.read().split("\n")

n, m = len(g), len(g[0])

x, y = 0, 0
for i in range(n):
	for j in range(m):
		if g[i][j] == 'S':
			x, y = i, j

adj = dict()
adj['F'] = [(1, 0), (0, 1)]
adj['7'] = [(1, 0), (0, -1)]
adj['L'] = [(-1, 0), (0, 1)]
adj['J'] = [(-1, 0), (0, -1)]
adj['|'] = [(1, 0), (-1, 0)]
adj['-'] = [(0, 1), (0, -1)]
adj['S'] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

q = []
d = [[-1 for j in range(m)] for i in range(n)]

d[x][y] = 0
q.append((x, y))
while q != []:
	r, c = q.pop(0)
	for dr, dc in adj[g[r][c]]:
		nr, nc = r + dr, c + dc
		if nr >= 0 and nr < n and nc >= 0 and nc < m:
			if g[nr][nc] != '.' and (-dr, -dc) in adj[g[nr][nc]] and d[nr][nc] == -1:
				d[nr][nc] = d[r][c] + 1
				q.append((nr, nc))

print(max(map(max, d)))