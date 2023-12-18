import sys

lines = sys.stdin.read().split("\n")

strength = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def compare(a, b):
	s1 = a.split()[0]
	s2 = b.split()[0]

	l1 = []
	for c in set(s1):
		if c != 'J':
			l1.append(s1.count(c))
	l2 = []
	for c in set(s2):
		if c != 'J':
			l2.append(s2.count(c))

	while len(l1) < 5: l1.append(0)
	while len(l2) < 5: l2.append(0)

	l1.sort(reverse = True)
	l2.sort(reverse = True)

	l1[0] += s1.count('J')
	l2[0] += s2.count('J')

	for i in range(len(l1)):
		if l1[i] > l2[i]:
			return 1
		if l1[i] < l2[i]:
			return -1

	for i in range(len(s1)):
		x, y = strength.index(s1[i]), strength.index(s2[i])
		if x < y:
			return 1
		if x > y:
			return -1
	return 0

lines.sort(cmp = compare)

ans = 0
for i, line in enumerate(lines):
	x, y = line.split()
	ans += (i + 1) * int(y)

print(ans)
