import sys

lines = sys.stdin.read().split("\n")

ans = 0
for line in lines:
	fir = next(x for x in line if x.isdigit())
	lst = next(x for x in line[::-1] if x.isdigit())
	ans += int(fir) * 10 + int(lst)

print(ans)
