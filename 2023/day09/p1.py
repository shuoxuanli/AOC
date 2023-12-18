import sys

lines = sys.stdin.read().split("\n")

ans = 0
for line in lines:
	line = map(int, line.split())
	l = [line]
	while l[-1].count(0) != len(l[-1]):
		cur = []
		for i in range(1, len(l[-1])):
			cur.append(l[-1][i] - l[-1][i - 1])
		l.append(cur)
	for i in range(len(l) - 1, 0, -1):
		l[i - 1].append(l[i - 1][-1] + l[i][-1])
	ans += l[0][-1]

print(ans)
