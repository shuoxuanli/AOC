import sys

g = sys.stdin.read().split("\n")

n, m = len(g), len(g[0])

def check(i, j):
    for x in range(-1, 2):
        for y in range(-1, 2):
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < m:
                if not g[ni][nj].isdigit() and g[ni][nj] != '.':
                    return True
    return False

ans = 0
for i in range(n):
    num = 0
    adj = False;
    for j in range(m + 1):
        if j < m and g[i][j].isdigit():
            adj = adj or check(i, j)
            num = num * 10 + int(g[i][j])
        else:
            if adj: ans += num
            adj = False
            num = 0

print(ans)
