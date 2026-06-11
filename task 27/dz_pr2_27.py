def center(cl):
    minn = 10**20
    p = None
    for x1, y1 in cl:
        s = 0
        for x2, y2 in cl:
            s += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if s < minn:
            minn = s
            p = (x1, y1)
    r = ((8 - p[0]) ** 2 + (4.5 - p[1]) ** 2) ** 0.5
    k = 0
    for x1, y1 in cl:
        if ((x1 - p[0]) ** 2 + (y1 - p[1]) ** 2) ** 0.5 <= 2.4:
            k += 1
    maxx = -(10**10)
    for x1, y1 in cl:
        s = ((p[0] - x1) ** 2 + (p[1] - y1) ** 2) ** 0.5
        if s > maxx:
            maxx = s
    return p[0], p[1], r, (k - 1), maxx


data1 = open("27_ADZ.txt").readlines()

data_a = []
for x in data1:
    s = [float(y) for y in x.replace(",", ".").split()]
    data_a.append(s)

cl1 = []
cl2 = []
for x, y in data_a:
    if x < 10:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

x1, y1, rcl1, kcl1, maxxcl1 = center(cl1)
x2, y2, rcl2, kcl2, maxxcl2 = center(cl2)

print("A:", min(len(cl1), len(cl2)), int((rcl1 + rcl2) * 10000))

data2 = open("27_BDZ.txt").readlines()

data_b = []
for x in data2:
    s = [float(y) for y in x.replace(",", ".").split()]
    data_b.append(s)

cl1 = []
cl2 = []
cl3 = []

for x, y in data_b:
    if 3 <= x <= 7 and 17 <= y <= 23:
        cl1.append((x, y))
    elif 7 <= x <= 12 and 6 <= y <= 13:
        cl2.append((x, y))
    elif 13 <= x <= 18 and 22 <= y <= 28:
        cl3.append((x, y))

print(len(cl1), len(cl2), len(cl3))
x1, y1, rcl1, kcl1, maxxcl1 = center(cl1)
x2, y2, rcl2, kcl2, maxxcl2 = center(cl2)
x3, y3, rcl3, kcl3, maxxcl3 = center(cl3)


print("B:", kcl3, int((maxxcl1) * 10000))