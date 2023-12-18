import sys

lines = sys.stdin.read().split("\n")

def check(i, j):
	for x in range(-1, 2):
		for y in range(-1, 2):
			ni = i + x
			nj = j + y
			if ni >= 0 and ni < len(lines) and nj >= 0 and nj < len(lines[0]):
				if not lines[ni][nj].isdigit() and lines[ni][nj] != '.':
					return True
	return False

ans = 0
for i in range(len(lines)):
	num = 0
	adj = False;
	for j in range(len(lines[i]) + 1):
		if j < len(lines[i]) and lines[i][j].isdigit():
			adj = adj or check(i, j)
			num = num * 10 + int(lines[i][j])
		else:
			if adj: ans += num
			adj = False
			num = 0

print(ans)
