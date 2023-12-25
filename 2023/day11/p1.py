import sys

g = sys.stdin.read().split("\n")

n, m, = len(g), len(g[0])

loc = []

r = [0] * n
for i in range(n):
    if sum(g[i][j] == '.' for j in range(m)) == m:
        r[i] = 1
    if i > 0: r[i] += r[i - 1]

c = [0] * m
for j in range(m):
    if sum(g[i][j] == '.' for i in range(n)) == n:
        c[j] = 1
    if j > 0: c[j] += c[j - 1]

for i in range(n):
    for j in range(m):
        if g[i][j] == '#':
            loc.append((i + r[i], j + c[j]))

ans = 0
for i in range(len(loc)):
    for j in range(i + 1, len(loc)):
        x1, y1 = loc[i]
        x2, y2 = loc[j]
        ans += abs(x1 - x2) + abs(y1 - y2)

print(ans)
