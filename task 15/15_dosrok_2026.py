p = [25, 64]
q = [40, 115]
otr = sorted(p + q)
ans = []
for a1 in otr:
    for a2 in otr:
        if a1 < a2:
            a = [a1, a2]
            f = 1
            for x in range(otr[0] - 10, otr[-1] + 10):
                if ((p[0] <= x <= p[-1]) <= (((q[0] <= x <= q[-1]) and (not(a[0] <= x <= a[-1]))) <= (not(p[0] <= x <= p[-1])))) == 0:
                    f = 0
                    break
            if f == 1:
                ans.append((a2 - a1, a))
print(min(ans))

print(257481 * (377 * 257486 + 67))
