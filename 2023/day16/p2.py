import sys

g = sys.stdin.read().split("\n")

n, m = len(g), len(g[0])

ch = [[0, 1], [-1, 0], [0, -1], [1, 0]]

def bfs(a, b, c):
	vis = [[[False for k in range(4)] for j in range(m)] for i in range(n)]
	q = [(a, b, c)]

	while q != []:
		x, y, d = q.pop(0)
		dx, dy = ch[d]
		nd = []
		nx, ny = x + dx, y + dy
		if nx >= 0 and nx < n and ny >= 0 and ny < m:
			if d % 2 == 0 and g[nx][ny] == '|':
				nd = [(d + 1) % 4, (d + 3) % 4]
			if d % 2 == 1 and g[nx][ny] == '-':
				nd = [(d + 1) % 4, (d + 3) % 4]
			if g[nx][ny] == '/':
				nd = [(d + 1) % 4 if d % 2 == 0 else (d + 3) % 4]
			if g[nx][ny] == '\\':
				nd = [(d + 3) % 4 if d % 2 == 0 else (d + 1) % 4]
			if nd == []: nd = [d]

			for ds in nd:
				if not vis[nx][ny][ds]:
					vis[nx][ny][ds] = True
					q.append((nx, ny, ds))

	return sum(vis[i][j][0] or vis[i][j][1] or vis[i][j][2] or vis[i][j][3] for i in range(n) for j in range(m))

ans = 0
for i in range(n):
	ans = max(ans, bfs(i, -1, 0))
	ans = max(ans, bfs(i, n, 2))

for i in range(m):
	ans = max(ans, bfs(-1, i, 3))
	ans = max(ans, bfs(m, i, 1))

print(ans)
