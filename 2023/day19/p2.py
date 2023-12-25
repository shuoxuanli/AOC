import sys
from copy import deepcopy

flow, item = sys.stdin.read().split("\n\n")

flow = {s[ : s.index("{")] : s[s.index("{") : ][1 : -1].split(",") for s in flow.split("\n")}

def rec(t, system):
    if t == "R" or t == "A":
        res = int(t == "A")
        if t == "A":
            for l, r in system.values():
                res = res * (r - l + 1) if l <= r else 0
        return res
    res = 0
    for v in flow[t]:
        if ":" in v:
            a, b = v.split(":")
            k, op, val = a[0], a[1], int(a[2 : ])
            l, r = system[k]
            if op == '<':
                system[k] = (l, min(r, val - 1))
                res += rec(b, deepcopy(system))
                system[k] = (max(l, val), r)
            else:
                system[k] = (max(l, val + 1), r)
                res += rec(b, deepcopy(system))
                system[k] = (l, min(r, val))
        else:
            res += rec(v, system)
    return res

print(rec("in", {'x' : (1, 4000), 'm' : (1, 4000), 'a' : (1, 4000), 's' : (1, 4000)}))
