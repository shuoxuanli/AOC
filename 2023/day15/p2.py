import sys

line = sys.stdin.read().split(",")

m = dict()
d = [[] for i in range(256)]

def hash(s):
	h = 0
	for x in s:
		h = (h + ord(x)) * 17 % 256
	return h

for s in line:
	if "-" in s:
		s = s[:-1]
		h = hash(s)
		if s in d[h]:
			d[h].remove(s)
	else:
		a, b = s.split('=')
		h = hash(a)
		m[a] = int(b)
		if a not in d[h]:
			d[h].append(a)

ans = 0
for i, x in enumerate(d, 1):
	for j, y in enumerate(x, 1):
		ans += i * j * m[y]

print(ans)
