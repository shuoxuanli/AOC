import sys

lines = sys.stdin.read().split("\n")

a = map(int, lines[0].split(":")[1].split())
b = map(int, lines[1].split(":")[1].split())

sa = int(''.join(map(str, a)))
sb = int(''.join(map(str, b)))

ans = 0
for i in range(sa + 1):
    if i * (sa - i) > sb:
        ans += 1

print(ans)
