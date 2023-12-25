import sys

lines = sys.stdin.read().split("\n\n")

num, lines = lines[0], lines[1:]
num = map(int, num.split(":")[1].split())

for line in lines:
    line = line.split(":\n")[1].split("\n")
    r = [map(int, v.split()) for v in line]
    for i in range(len(num)):
        for a, b, c in r:
            if num[i] >= b and num[i] <= b + c - 1:
                num[i] = a + num[i] - b
                break

print(min(num))
