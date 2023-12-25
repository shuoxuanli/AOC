import sys

lines = sys.stdin.read().split("\n")

num = "0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine".split()

ans = 0
for line in lines:
    fir = min(num, key = lambda x : line.index(x) if x in line else len(line))
    lst = min(num, key = lambda x : line[::-1].index(x[::-1]) if x in line else len(line))
    ans += num.index(fir) // 2 * 10 + num.index(lst) // 2

print(ans)
