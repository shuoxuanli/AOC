import sys

line = sys.stdin.read().split(",")

def hash(s):
	h = 0
	for x in s:
		h = (h + ord(x)) * 17 % 256
	return h

print(sum(map(hash, line)))
