import sys

lines = sys.stdin.read().split("\n")

a = map(int, lines[0].split(":")[1].split())
b = map(int, lines[1].split(":")[1].split())

ans = 1
for i in range(len(a)):
	ways = 0
	for j in range(a[i] + 1):
		if j * (a[i] - j) > b[i]:
			ways += 1
	ans *= ways

print(ans)
