import sys

dir, lines = sys.stdin.read().split("\n\n")
maps = [x.split(" = ") for x in lines.split("\n")]
maps = {a : b[1 : -1].split(", ") for a, b in maps}

cur = "AAA"
p, ans = 0, 0

while cur != "ZZZ":
    cur = maps[cur][dir[p] == 'R']
    ans += 1
    p = (p + 1) % len(dir)

print(ans)
