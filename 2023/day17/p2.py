import sys, heapq

g = sys.stdin.read().split("\n")
g = [map(int, row) for row in g]

n, m = len(g), len(g[0])

dis = dict()

pq = [(0, 0, 0, -1, 0)]

while pq:
    v, x, y, d, c = heapq.heappop(pq)
    if (x, y, d, c) in dis:
        continue
    dis[(x, y, d, c)] = v
    for i, (dx, dy) in enumerate([[0, 1], [1, 0], [0, -1], [-1, 0]]):
        nx, ny = x + dx, y + dy
        nc = 1 if d != i else c + 1
        if nc <= 10 and (d == i or d == -1 or c >= 4) and (i + 2) % 4 != d and 0 <= nx < n and 0 <= ny < m:
            heapq.heappush(pq, (v + g[nx][ny], nx, ny, i, nc))

ans = 1E9
for (x, y, d, c), v in dis.items():
    if x == n - 1 and y == m - 1 and c >= 4:
        ans = min(ans, v)

print(ans)
