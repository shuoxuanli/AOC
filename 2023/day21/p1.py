import sys

g = sys.stdin.read().split("\n")

n, m = len(g), len(g[0])

x, y = next((i, j) for i, a in enumerate(g) for j, b in enumerate(a) if b == 'S')

q = [(x, y, 64)]
s = set((x, y, 64))

ans = 0
while q:
    x, y, d = q.pop(0)
    if d == 0:
        ans += 1
        continue
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#':
            if (nx, ny, d - 1) not in s:
                s.add((nx, ny, d - 1))
                q.append((nx, ny, d - 1))

print(ans)
