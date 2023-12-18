import sys

lines = sys.stdin.read().split("\n")

ans = 0
for line in lines:
	ID, sets = line.split(": ")
	r, g, b = 0, 0, 0
	for x in sets.split("; "):
		nx = [i.split() for i in x.split(", ")]
		mp = {b : int(a) for a, b in nx}
		r = max(r, mp.get("red", 0))
		g = max(g, mp.get("green", 0))
		b = max(b, mp.get("blue", 0))
	ans += r * g * b

print(ans)
