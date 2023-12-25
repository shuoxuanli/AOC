import sys
from math import lcm

dir, lines = sys.stdin.read().split("\n\n")
maps = [x.split(" = ") for x in lines.split("\n")]
maps = {a : b[1 : -1].split(", ") for a, b in maps}

ans = []
for cur in maps:
    if cur[-1] != 'A':
        continue
    p, cnt = 0, 0
    while cur[-1] != 'Z':
        cur = maps[cur][dir[p] == 'R']
        cnt += 1
        p = (p + 1) % len(dir)
    ans.append(cnt)

print(lcm(*ans))
