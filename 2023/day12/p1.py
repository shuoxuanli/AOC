import sys

lines = sys.stdin.read().split("\n")
	
ans = 0
for line in lines:
	s, a = line.split()
	a = map(int, a.split(','))
	n, m = len(s), len(a)
	dp = [[[0 for k in range(2)] for j in range(m + 1)] for i in range(n + 1)]
	dp[0][0][0] = 1
	for i in range(n):
		for j in range(m + 1):
			ok = True
			if s[i] != '#':
				dp[i + 1][j][0] += dp[i][j][0]
				dp[i + 1][j][0] += dp[i][j][1]
			if j < m:
				for k in range(a[j]):
					ok = ok and i + k < n and s[i + k] != '.'
				if ok:
					dp[i + a[j]][j + 1][1] += dp[i][j][0]
	ans += dp[n][m][0] + dp[n][m][1]

print(ans)
