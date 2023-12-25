import sys

flow, item = sys.stdin.read().split("\n\n")

flow = {s[ : s.index("{")] : s[s.index("{") : ][1 : -1].split(",") for s in flow.split("\n")}

def rec(t, system):
    if t == 'R' or t == 'A':
        return t == 'A'

    for v in flow[t]:
        if ":" in v:
            a, b = v.split(":")
            k, op, val = a[0], a[1], int(a[2 : ])
            if op == '>' and system[k] > val:
                return rec(b, system)
            if op == '<' and system[k] < val:
                return rec(b, system)
        else:
            return rec(v, system)

ans = 0
for v in item.split("\n"):
    system = {p.split("=")[0] : int(p.split("=")[1]) for p in v[1 : -1].split(",")}
    if rec("in", system):
        ans += sum(system.values())

print(ans)
