import sys

g = sys.stdin.read().split("\n")

n, m = len(g), len(g[0])

g = [list(s) for s in g]

def work(g):
    for j in range(m):
        for i in range(n):
            if g[i][j] == 'O':
                x = i
                while x > 0 and g[x - 1][j] == '.':
                    g[x][j], g[x - 1][j] = g[x - 1][j], g[x][j]
                    x -= 1

    for i in range(n):
        for j in range(m):
            if g[i][j] == 'O':
                x = j
                while x > 0 and g[i][x - 1] == '.':
                    g[i][x], g[i][x - 1] = g[i][x - 1], g[i][x]
                    x -= 1

    for j in range(m):
        for i in range(n - 1, -1, -1):
            if g[i][j] == 'O':
                x = i
                while x < n - 1 and g[x + 1][j] == '.':
                    g[x][j], g[x + 1][j] = g[x + 1][j], g[x][j]
                    x += 1

    for i in range(n):
        for j in range(m - 1, -1, -1):
            if g[i][j] == 'O':
                x = j
                while x < m - 1 and g[i][x + 1] == '.':
                    g[i][x], g[i][x + 1] = g[i][x + 1], g[i][x]
                    x += 1

d = dict()
cnt, turn = 0, 1000000000

while True:
    t = ''.join([''.join(s) for s in g])
    if t in d:
        cnt -= d[t]
        break

    d[t] = cnt
    work(g)

    cnt += 1
    turn -= 1

for i in range(turn % cnt):
    work(g)

print(sum(n - i for i in range(n) for j in range(m) if g[i][j] == 'O'))
