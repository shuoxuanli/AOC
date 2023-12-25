import sys

lines = sys.stdin.read().split("\n")

ans = 0
for line in lines:
    l = [map(int, line.split())]
    while not all(x == 0 for x in l[-1]):
        l.append([l[-1][i] - l[-1][i - 1] for i in range(1, len(l[-1]))])
    for i in range(len(l)):
        l[i] = l[i][::-1]
    for i in range(len(l) - 1, 0, -1):
        l[i - 1].append(l[i - 1][-1] - l[i][-1])
    ans += l[0][-1]

print(ans)
