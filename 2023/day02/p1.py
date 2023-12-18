import sys

lines = sys.stdin.read().split("\n")

ans = 0
for line in lines:
	ID, sets = line.split(": ")
	for x in sets.split("; "):
		nx = [i.split() for i in x.split(", ")]
		mp = {b : int(a) for a, b in nx}
		if mp.get("red", 0) > 12 or mp.get("green", 0) > 13 or mp.get("blue", 0) > 14:
			break
	else:
		ans += int(ID.split()[-1])

print(ans)
