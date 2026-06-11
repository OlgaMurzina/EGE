t1 = open('9.csv').readlines()
t = []
for s in t1:
    t.append([int(x) for x in s.split(';')])
print(t[:10])

k = 0
for s in t:
    st = sorted(s)
    if (st[0] + st[-1]) ** 2 > st[1] ** 2 + st[2] ** 2 + st[3] ** 2:
        k += 1
print(k)