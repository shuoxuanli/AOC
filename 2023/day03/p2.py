import sys

g = sys.stdin.read().split("\n")

n, m = len(g), len(g[0])

s = []
for i in range(n):
    num = 0
    for j in range(m + 1):
        if j < m and g[i][j].isdigit():
            num = num * 10 + int(g[i][j])
        else:
            if num != 0:
                s.append([i, j - len(str(num)), j - 1, num])
                num = 0

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '*':
            lis = []
            for k in range(-1, 2):
                for l in range(-1, 2):
                    for p in range(len(s)):
                        r, x, y, z = s[p]
                        if r == i + k and x <= j + l <= y and p not in lis:
                            lis.append(p)
            if len(lis) == 2: ans += s[lis[0]][3] * s[lis[1]][3]

print(ans)
