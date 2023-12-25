import sys

lines = sys.stdin.read().split("\n")

ans = 0
for line in lines:
    line = line.split(": ")[1]
    a, b = line.split("|")
    a, b = a.split(), b.split()
    s = sum(x in a for x in b)
    if s > 0: ans += 2 ** (s - 1)

print(ans)
