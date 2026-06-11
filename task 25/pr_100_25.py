def good(x):
    de = []
    for d in range(2, round(x ** 0.5) + 1):
        if x % d == 0:
            de.append(d)
            if x //d not in de:
                de.append(x // d)
    de = sorted(de)
    dn = de[-6] if len(de) >= 6 else 0
    return dn, len(de)

ans = []
n = 300_000_001
while len(ans) < 5:
    y = good(n)
    if y[0]:
        ans.append(y)
        print(y[0], y[1])
    n += 1
