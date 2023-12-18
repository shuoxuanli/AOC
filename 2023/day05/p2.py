import sys

lines = sys.stdin.read().split("\n\n")

num, lines = lines[0], lines[1:]
num = map(int, num.split(":")[1].split())

num = [[num[i], num[i] + num[i + 1] - 1] for i in range(0, len(num), 2)]

for line in lines:
	line = line.split(":\n")[1].split("\n")
	rng = [map(int, v.split()) for v in line]
	lis = num[:]
	for l, r in num:
		cur = [[l - 1, l - 1], [r + 1, r + 1]]
		for a, b, c in rng:
			if r >= b and l <= b + c - 1:
				L = max(b, l)
				R = min(r, b + c - 1)
				cur.append([L, R])
				lis.append([L - b + a, R - b + a])
		cur.sort()
		lis.remove([l, r])
		for i in range(len(cur) - 1):
			l1, r1 = cur[i]
			l2, r2 = cur[i + 1]
			if r1 + 1 <= l2 - 1:
				lis.append([r1 + 1, l2 - 1])
	num = lis

print(min([l for l, r in num]))
