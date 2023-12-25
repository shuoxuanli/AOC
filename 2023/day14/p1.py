import sys

g = sys.stdin.read().split("\n")

n, m = len(g), len(g[0])

g = [list(s) for s in g]

ans = 0
for j in range(m):
    for i in range(n):
        if g[i][j] == 'O':
            x = i
            while x > 0 and g[x - 1][j] == '.':
                g[x][j], g[x - 1][j] = g[x - 1][j], g[x][j]
                x -= 1
            ans += n - x

print(ans)
