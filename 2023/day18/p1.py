import sys

lines = sys.stdin.read().split("\n")

pt = [(x, y)]
p, x, y = 0, 0, 0

for line in lines:
    a, b, c = line.split()
    b = int(b)
    p += b
    if a == 'R':
        y += b
    elif a == 'D':
        x += b
    elif a == 'L':
        y -= b
    else:
        x -= b
    pt.append((x, y))

ans = 0
for i in range(len(pt)):
    x1, y1 = pt[i]
    x2, y2 = pt[(i + 1) % len(pt)]
    ans += x1 * y2 - x2 * y1
ans = abs(ans) // 2 + p // 2 + 1

print(ans)
