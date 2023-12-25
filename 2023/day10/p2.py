import sys

g = sys.stdin.read().split("\n")

n, m = len(g), len(g[0])

x, y = next((i, j) for i, a in enumerate(g) for j, b in enumerate(a) if b == 'S')

adj = dict()
adj['.'] = []
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
        if 0 <= nr < n and 0 <= nc < m:
            if g[nr][nc] != '.' and (-dr, -dc) in adj[g[nr][nc]] and d[nr][nc] == -1:
                d[nr][nc] = d[r][c] + 1
                q.append((nr, nc))

ng = [['.' for j in range(2 * m)] for i in range(2 * n)]

for i in range(n):
    for j in range(m):
        if d[i][j] != -1:
            ng[i * 2][j * 2] = g[i][j]
            if i < n - 1 and d[i + 1][j] != -1 and (1, 0) in adj[g[i][j]] and (-1, 0) in adj[g[i + 1][j]]:
                ng[i * 2 + 1][j * 2] = '|'
            if j < m - 1 and d[i][j + 1] != -1 and (0, 1) in adj[g[i][j]] and (0, -1) in adj[g[i][j + 1]]:
                ng[i * 2][j * 2 + 1] = '-'
g = ng

v = [[False for j in range(2 * m)] for i in range(2 * n)]

def bfs(x, y):
    q = [(x, y)]
    res = 0
    ok = True
    v[x][y] = True
    while q != []:
        r, c = q.pop(0)
        res += r % 2 == 0 and c % 2 == 0
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < 2 * n and 0 <= nc < 2 * m):
                ok = False
                continue
            if not v[nr][nc] and g[nr][nc] == '.':
                v[nr][nc] = True
                q.append((nr, nc))
    return ok * res

ans = 0
for i in range(n):
    for j in range(m):
        if not v[i][j] and g[i][j] == '.':
            ans += bfs(i, j)

print(ans)
